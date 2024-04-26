from django.urls import path
from . import views

urlpatterns = [
    path("", views.lawList, name="wiki"),
    # path("laws/", views.lawList, name="laws")
 ]