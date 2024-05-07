from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('ALogin/', views.loginA, name="AbogadoLogin"),
    path('ASignUp/', views.signupA, name="AbogadoSignUp"),
    path('ASignUp2/', views.signupA2, name="AbogadoSignUp2"),
    path('Profile/', views.checkProfile, name="Abogado Profile")
]