from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('createAbugado/', views.createAbugado),
    path('ALogin/', views.loginA, name="AbugadoLogin"),
    path('ASignUp/', views.signupA, name="AbugadoSignUp"),
    path('AHomepage/', views.homepageA, name="AbugadoHomepage"),
    path('Profile/', views.checkProfile, name="Abugado Profile")
]