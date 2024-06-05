from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('createManggagawa/', views.createAbogado),
    path('Mlogin/', views.loginM, name="ManggagawaLogin"),
    path('MSignUp/', views.signupM, name="ManggagawaSignUp"),
    path('MHomepage/', views.homepageM, name="ManggagawaHomepage"),
    path('MSubmitcase/', views.submitcaseM, name="ManggagawaSubmitcase"),
    path('MSignUp2/', views.signupM2, name="ManggagawaSignUp2"),
    #path('Profile/<int:m_id>/', views.Profile, name="MProfile")
    #path('Profile/', views.checkProfile, name="Abogado Profile")
]