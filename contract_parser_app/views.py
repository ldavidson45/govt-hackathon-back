from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .parse_script import parse_document
from django.http import JsonResponse


# Create your views here.


# accept a word document and return data 

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print ("valid form")
            parsed_doc = parse_document(request.FILES['file'])
        return redirect(request, 'contract_parser/contract_show.html', {"contract": parsed_doc})
    else:
        form = UploadFileForm()
    return (request, 'contract_parser/file_upload.html', {'form': form})

def contract_detail(request):
    return render(request, 'contract_parser/contract_show.html')