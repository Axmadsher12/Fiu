"""
URL configuration for djangofile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myfiles.views import *
from djangofile import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_in/',sign_in,name='sign_in'),
    path('sign_up/',sign_up,name='sign_up'),
    path('logout/',user_logout,name='logout'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('design/',design,name='design'),
    path('',index,name='index'),
    path('shop/',shop,name='shop'),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL,document_root = settings.MEDIAFILES_DIRS)
