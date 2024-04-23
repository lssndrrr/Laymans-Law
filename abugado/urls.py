from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('createAbugado/', views.createAbugado),
    path('abugadoLogin/', views.loginA, name="AbugadoLogin"),
    path('Profile/', views.checkProfile, name="Abugado Profile")
]