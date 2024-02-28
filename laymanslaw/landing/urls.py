from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.landing),
    #path('login/manggagawa', views.loginM),
    #path('login/abugado', views.loginA)
]