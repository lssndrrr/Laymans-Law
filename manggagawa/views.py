from django.shortcuts import render
from .models import Manggagawa

# Create your views here.

def loginM(request):
    if request.method == "GET":
        return render(request, "manggagawa/laymen_login.html")
    # try:
    #     password=request.POST.get("password")
    #     profile=ProfileM.objects.get(email_add=request.POST.get("email_add"))
        
    #     if profile.password == password:
    #         #return render(request, "abogado/abogado_profile.html", {"profile": profile, })
    #         pass
    #     else:
    #            #return render(request, "man/sign_up.html")
    #         pass
    # except:
    #     #return render(request, "abogado/sign_up.html")
    #     pass

def signupM(request):
    return render(request, "manggagawa/laymen_signup.html")