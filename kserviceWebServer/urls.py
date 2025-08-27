"""
URL configuration for kserviceWebServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as login
from imageLoader import views as imageLoader
from complemedica import views as complemedica
from pabon import views as pabon
from teleperformance import views as teleperformance

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("login", login.login,name='login'),
    path("imageLoader", imageLoader.imageDownload ,name='imageLoader'),
    path("jsonImages", imageLoader.jsonFiles ,name='jsonFiles'),
    path("complemedica/imageLoader", complemedica.imageDownload ,name='imageLoader'),
    path("complemedica/jsonImages", complemedica.jsonFiles ,name='jsonFiles'),
    path("pabon/imageLoader", pabon.imageDownload ,name='imageLoader'),
    path("pabon/jsonImages", pabon.jsonFiles ,name='jsonFiles'),
    path("teleperformance/imageLoader", teleperformance.imageDownload ,name='imageLoader'),
    path("teleperformance/jsonImages", teleperformance.jsonFiles ,name='jsonFiles'),
]
