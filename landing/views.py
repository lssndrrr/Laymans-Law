from django.shortcuts import render, redirect
from abogado.models import Abogado
from abogado.views import ProfileA
from manggagawa.views import ProfileM

# Create your views here.

def landing(request):
    if request.method == "GET" and request.user.is_authenticated:
        if request.user.user_type == 'abogado':
            return redirect(ProfileA, request.user.abogado.roll_number)
        elif request.user.user_type == 'manggagawa':
            return redirect(ProfileM, request.user.manggagawa.m_id)
    else:
        return render(request, "landing/landing_page.html")
    