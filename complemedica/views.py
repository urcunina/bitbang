from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.conf import settings
from natsort import os_sorted
from django.http import JsonResponse
import os
import socket
import aiofiles

def get_ip_from_domain():
    try:
        ip = socket.gethostbyname("kservice.com.co")
        return ip
    except socket.gaierror:
        return None

# def imageDownload(request):
#     filename = request.GET.get('filename',"")
#     image_path = str(settings.BASE_DIR)+'/imageLoader/static/img/'+str(filename)    
#     # print(dir_list)
#     # print(image_path)
#     image_data = open(image_path, "rb")    
#     return FileResponse(image_data, content_type="image/jpeg")

async def imageDownload(request):
    filename = request.GET.get('filename', "")
    image_path = os.path.join(settings.BASE_DIR, 'complemedica/static/img', filename)

    async def file_iterator(path, chunk_size=8192):
        async with aiofiles.open(path, 'rb') as f:
            while True:
                chunk = await f.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    return StreamingHttpResponse(file_iterator(image_path), content_type="image/jpeg")

def jsonFiles(request):
    dir_list = os_sorted(os.listdir(str(settings.BASE_DIR)+'/complemedica/static/img'))
    auxString=''
    for sa in range(0,len(dir_list)):
        if sa==0:
            auxString=str(dir_list[sa])
        else:
            auxString=auxString+','+str(dir_list[sa])

    context= {
                'imagenes' : auxString,
                'ipResolve': get_ip_from_domain(),
                'operadores': "complemedica-1@kservice.com.co"
            }
    return JsonResponse(context)
