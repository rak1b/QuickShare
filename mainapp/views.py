from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import shutil
# Create your views here.
from .models import Folder, Files
import json


def homeview(request):
    return render(request, "main/home.html")


def download_files(request, uid):
    url = {'url': f"{request.scheme }://{ request.META.get('HTTP_HOST')}/static/zip/{uid}.zip"}
    return render(request, 'main/download.html', context=url)


def zip_files(folder):
    shutil.make_archive(f'static/zip/{folder}', 'zip', f'media/{folder}')


def upload_files(request):

    if request.method == 'POST':

        files = request.FILES.values()
        folder = Folder.objects.create()
        files_objs = []
        for file in files:
            # print("files", file)
            files_obj = Files.objects.create(folder=folder, file=file)
            files_objs.append(files_obj)

        zip_files(folder.uid)
        # return JsonResponse({'uid': folder.uid})
        return JsonResponse({'download_url': f"{request.scheme }://{ request.META.get('HTTP_HOST')}/download/{folder.uid}"})
