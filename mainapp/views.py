from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import shutil,os
from .models import Folder, Files
import json
from .utils import get_time_diff
from django.conf import settings

def homeview(request):
    return render(request, "main/home.html")


def download_files(request, uid):
    folder = Folder.objects.filter(uid=uid).first()
    if folder is None:
        return HttpResponse("Invalid link")
    else:
        if folder.private:
            if request.method == 'POST':
                passw = request.POST.get('password')
                if passw == folder.password:
                    context = {
                        "message": "Success,Click the button to download files",
                        'url': f"{request.scheme }://{ request.META.get('HTTP_HOST')}/static/zip/{uid}.zip"
                    }
                else:
                    context = {
                        "message": "Error,Invalid Pasword",
                        'url': "",
                        "input": True,

                    }
            else:
                context = {
                    "message":  "This is a private file. Please enter the password to download the files",
                    'url': "",
                    "input": True,
                }
        else:
            context = {
                "message": "Click The Button To Download Your Files",
                'url': f"{request.scheme }://{ request.META.get('HTTP_HOST')}/static/zip/{uid}.zip"
            }
    return render(request, 'main/download.html', context=context)


def zip_files(folder):
    base = settings.BASE_DIR
    shutil.make_archive(f'{base}/static/zip/{folder}', 'zip', f'{base}/media/{folder}')


def upload_files(request):

    if request.method == 'POST':
        print("request.POST", request.POST)
        passw = request.POST.get('password')
        print("passw -- > ", passw)
        files = request.FILES.values()
        if passw is not None and len(passw) > 0:
            folder = Folder.objects.create(password=passw, private=True)
        else:
            folder = Folder.objects.create()
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder=folder, file=file)
            files_objs.append(files_obj)

        zip_files(folder.uid)
        shutil.rmtree(f'media/{folder.uid}')
        return JsonResponse({'download_url': f"{request.scheme }://{ request.META.get('HTTP_HOST')}/download/{folder.uid}"})


def delete_files(request):
    folders = Folder.objects.all()
    for folder in folders:
        diff = get_time_diff(folder)

        print(diff)
    return HttpResponse("Deleted")


def delete_single(request, uid):
    folder = Folder.objects.filter(uid=uid).delete()
    os.remove(f"static/zip/{uid}.zip")
    return HttpResponse("Deleted")
    # if folder.uid == uid:
    #     shutil.rmtree(f'media/{folder.uid}')

def FileUploadView(request):
    return render(request, 'main/upload/upload_page.html')
