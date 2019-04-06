from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
# from .parse_script import parse_document

# Create your views here.


# accept a word document and return data 

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # parse_document(request.FILES['file'])
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'contract_parser/file_upload.html', {'form': form})
