from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
# from .parse_script import parse_document

# Create your views here.


# accept a word document and return data 

def upload_file(request):
    if request.method == 'POST':
        print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # parse_document(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        print(request.FILES)
        form = UploadFileForm()
    return render(request, 'contract_parser/file_upload.html', {'form': form})
