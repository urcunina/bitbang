from django.shortcuts import render
from django.template import Template, Context
from django.contrib.auth import aauthenticate 
from django.contrib.auth import alogin, alogout
from django.shortcuts import redirect
from  django.http import HttpRequest as request
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User

async def login(request):

    if request.method == 'GET':
        return render(request, 'pages/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if (username is not None) and (password is not None ):
            auser=await aauthenticate(username=username,password=password)         
            if auser is not None:   
                await alogin(request,auser)          
                context= {
                'message': auser,
                }
                return redirect("/home")
                return render(request, 'pages/login.html', context)
            else:
                context= {
                'message': "Nombre de usuario o contraseña incorrecta",
                }
                return render(request, 'pages/login.html', context)
        else:
            context= {
            'message': "Digite su usuario y contraseña",
            }
            return render(request, 'pages/login.html', context)
    else:
        context= {
        'message': "",
        }
        return render(request, 'pages/login.html', context)



