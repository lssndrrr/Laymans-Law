from django.shortcuts import render
from .models import Manggagawa

# Create your views here.

def loginM(request):
    if request.method == "GET":
        return render(request, "manggagawa/login_worker.html")
    # try:
    #     password=request.POST.get("password")
    #     profile=ProfileM.objects.get(email_add=request.POST.get("email_add"))
        
    #     if profile.password == password:
    #         #return render(request, "abugado/abugado_profile.html", {"profile": profile, })
    #         pass
    #     else:
    #            #return render(request, "man/sign_up.html")
    #         pass
    # except:
    #     #return render(request, "abugado/sign_up.html")
    #     pass