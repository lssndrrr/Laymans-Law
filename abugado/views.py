from django.shortcuts import render
from .models import Abugado, Cases
from django.http import HttpResponse

# Create your views here.
def createAbugado(request):
    if request.method == "POST":
        # Profile.objects.create(name=request.data.name)
        print(request)
        #return HttpResponse(request)

def loginA(request):
    if request.method == "GET":
        return render(request, "abugado/lawyer_login.html")
    try:
        password=request.POST.get("password")
        profile=Abugado.objects.get(email_add=request.POST.get("email_add"))
        
        if profile.password == password:
            # return render(request, "abugado/abugado_profile.html", {"profile": profile, })
            pass
        else:
           # return render(request, "abugado/sign_up.html")
            pass
    except:
        # return render(request, "abugado/sign_up.html")
        pass

def signupA(request):
    if request.method == "GET":
        return render(request, "abugado/lawyer_signup.html")
    return render(request, "abugado/lawyer_signup.html")
    
def checkProfile(request):
    pass