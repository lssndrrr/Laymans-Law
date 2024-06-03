from django.urls import path
from . import views

urlpatterns = [
    path('WPrelim/', views.prelimW, name="WikiPrelim"),
    # path("laws/", views.lawList, name="laws")
 ]
