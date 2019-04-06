from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .parse_script import parse_document
from django.http import JsonResponse
from .models import Contract


# Create your views here.


# accept a word document and return data 

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print ("valid form")
            parsed_doc = parse_document(request.FILES['file'])
            print(parsed_doc)
            db_doc = Contract.objects.create({
                'description': parsed_doc['Description'],
                'background': parsed_doc['BACKGROUND'],
                'required_services': parsed_doc['REQUIRED SERVICES'],
                'response_detail': parsed_doc['RESPONSES'],
                'title': parsed_doc['PWS']
            })
            # save parsed_doc to DB through model
            # send back instance from model (which will include the ID)
        return JsonResponse(db_doc, safe=False)
        # return render(request, 'contract_parser/contract_show.html', {"contract": parsed_doc})
    else:
        form = UploadFileForm()
    return render(request, 'contract_parser/file_upload.html', {'form': form})

def contract_detail(request, pk):
    # Third:
    # Look up item from db
    return render(request, 'contract_parser/contract_show.html')
