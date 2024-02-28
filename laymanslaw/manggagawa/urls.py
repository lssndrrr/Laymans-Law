from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('createManggagawa/', views.createAbugado),
    path('manggagawaLogin/', views.loginM, name="ManggagawaLogin"),
    #path('Profile/', views.checkProfile, name="Abugado Profile")
]