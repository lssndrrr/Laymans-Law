from django.urls import path
from . import views

urlpatterns = [
    path('wiki/', views.Wiki, name="Wiki"),
    # path("laws/", views.lawList, name="laws")
 ]
