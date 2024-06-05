from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('createManggagawa/', views.createAbogado),
    path('login/', views.loginM, name="ManggagawaLogin"),
    path('signup/', views.signupM, name="ManggagawaSignUp"),
    path('registration/', views.signupM2, name="ManggagawaSignUp2"),
    path('profile/<int:m_id>/', views.ProfileM, name="MProfile")
    #path('Profile/', views.checkProfile, name="Abogado Profile")
]