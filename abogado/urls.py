from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('ALogin/', views.loginA, name="AbogadoLogin"),
    path('ASignUp/', views.signupA, name="AbogadoSignUp"),
    path('ASignUp2/', views.signupA2, name="AbogadoSignUp2"),
    # path('AHomepage/', views.homepageA, name="AbogadoHomepage"),
    path('Profile/<int:roll_number>/', views.Profile, name="AProfile"),
    path('Profile/<int:roll_number>/Settings/', views.ASettings, name="SettingsA"),
]