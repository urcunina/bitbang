from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
from natsort import os_sorted
from django.http import JsonResponse
import os

def imageDownload(request):
    filename = request.GET.get('filename',"")

    image_path = str(settings.BASE_DIR)+'/imageLoader/static/img/'+str(filename)    
    # print(dir_list)
    # print(image_path)
    image_data = open(image_path, "rb")    
    return FileResponse(image_data, content_type="image/jpeg")

def jsonFiles(request):
    dir_list = os_sorted(os.listdir(str(settings.BASE_DIR)+'/imageLoader/static/img'))
    auxString=''
    for sa in range(0,len(dir_list)):
        if sa==0:
            auxString=str(dir_list[sa])
        else:
            auxString=auxString+','+str(dir_list[sa])

    context= {
                'imagenes' : auxString
            }
    return JsonResponse(context)
