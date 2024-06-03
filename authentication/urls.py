from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('SPassword/', views.passwordS, name="SettingsPassword"),
    path('SAccount/', views.passwordA, name="SettingsAccount"),
]