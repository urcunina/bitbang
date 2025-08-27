from django.shortcuts import render
import os
from natsort import os_sorted
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

baseUrl="http://127.0.0.1:8000/teleperformance/imageLoader?filename="
htmlBase1= '<div class="item"><img src="'
htmlBase2= ' " data-id="'
htmlBase3= '"><button class="delete-btn" data-id="'
htmlBase4= '">🗑️</button></div>'

def objetoImagen(urlImage,index):
    htmlObjeto=htmlBase1+urlImage+htmlBase2+str(index)+htmlBase3+str(index)+htmlBase4
    return htmlObjeto

def jsonFiles():
    dir_list = os_sorted(os.listdir(str(settings.BASE_DIR)+'/teleperformance/static/img/'))
    auxString=''
    for sa in range(0,len(dir_list)):
        if sa==0:
            auxString=str(dir_list[sa])
        else:
            auxString=auxString+','+str(dir_list[sa])
    return auxString

@csrf_exempt  # ⚠️ solo si no usas CSRFToken en fetch (no recomendado en producción)
def deleteItem(request):
    if request.method == "POST":
        item_id = request.POST.get("id")  # <-- Aquí recibes el ID
        if item_id:
            files=jsonFiles()
            try:
                os.remove(str(settings.BASE_DIR)+'/teleperformance/static/img/'+files.split(',')[int(item_id)])
            except:
                 pass
            # print(str(settings.BASE_DIR)+'/teleperformance/static/img/'+files.split(',')[int(item_id)])

            return JsonResponse({"success": True, "deleted_id": item_id})
        return JsonResponse({"success": False, "error": "ID no recibido"})
    return JsonResponse({"success": False, "error": "Método no permitido"})

@csrf_exempt
def uploadImage(request):
    if request.method == "POST":
        imagen = request.FILES.get("imagen")
        if imagen:
            # Puedes guardarla en el sistema de archivos
            with open(str(settings.BASE_DIR)+'/teleperformance/static/img/' + imagen.name, "wb+") as destino:
                for chunk in imagen.chunks():
                    destino.write(chunk)
            return JsonResponse({"message": "ok", "filename": imagen.name})
        return JsonResponse({"error": "No se recibió ninguna imagen"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
     

# @login_required
async def imagemanager(request):
    images=jsonFiles()
    print(images)
    url=""
    for i in range(0, len(images.split(','))):
        if i !=0:
            url=url+","+baseUrl+images.split(',')[i]
        else:
             url=baseUrl+images.split(',')[i]
    print(url)
    # Creamos el HTML con las imágenes
    html=""
    for i in range(0,len(url.split(','))):
         html+=objetoImagen(url.split(',')[i],i)
    print(html)
         
    if request.method == 'GET':
                context= {
                'imagenes': html,
                }
                return render(request, 'pages/imagemanager.html', context)


