from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('SPasswordAB/', views.settingsPA, name="SettingsPasswordLawyer"),
    path('SAccountAB/', views.settingsAA, name="SettingsAccountLawyer"),
    path('SPasswordMG/', views.settingsPM, name="SettingsPasswordLaymen"),
    path('SAccountMG/', views.settingsAM, name="SettingsAccountLaymen"),   
]