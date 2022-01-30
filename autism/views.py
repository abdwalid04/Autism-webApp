from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


#function to handle an uploaded file.
from .cnn import cnn

def index(request):
    return render(request,'autism/index.html')

def upload(request):
    # if request.method == 'POST' and 'descripteurBtn' in request.POST:
    #     upload = request.FILES['upload']
    #     fss = FileSystemStorage()
    #     file = fss.save(upload.name, upload)
    #     file_url = fss.url(file)
    #     descripteur = request.POST['descripteur']
    #     distance=request.POST['distance']
    #     img_path='.'+file_url
    #     classe = test(img_path,mat_image, distance , descripteur)
    #     context={'classe': classe,'file_url':file_url}
    #     return render(request, 'autism/upload.html', context)
    if request.method == 'POST' and  'cnnBtn' in request.POST:
        upload1 = request.FILES['upload1']
        fss = FileSystemStorage()
        file = fss.save(upload1.name, upload1)
        file_url = fss.url(file)
        img_path='.'+file_url
        classe = cnn(img_path)
        context={'classe': classe,'file_url':file_url}
        return render(request, 'autism/upload.html', context)
    return render(request, 'autism/upload.html')