from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('createManggagawa/', views.createAbogado),
    path('Mlogin/', views.loginM, name="ManggagawaLogin"),
    path('MSignUp/', views.signupM, name="ManggagawaSignUp"),
    path('MHomepage/', views.homepageM, name="ManggagawaHomepage"),
    path('MSubmitcase/', views.submitcaseM, name="ManggagawaSubmitcase"),
    #path('Profile/', views.checkProfile, name="Abogado Profile")
]