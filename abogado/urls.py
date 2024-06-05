from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('login/', views.loginA, name="AbogadoLogin"),
    path('signup/', views.signupA, name="AbogadoSignUp"),
    path('registration/', views.signupA2, name="AbogadoSignUp2"),
    # path('Profile/<int:roll_number>/', views.Profile, name="AProfile")
    # path('AHomepage/', views.homepageA, name="AbogadoHomepage"),
    path('profile/<int:roll_number>/', views.ProfileA, name="AProfile"),
    path('profile/<int:roll_number>/settings/', views.ASettings, name="SettingsA"),
    
    path('logout/', views.logout_view, name = "AbogadoLogout"),
]