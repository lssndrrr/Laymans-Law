from django.shortcuts import render

# Create your views here.
def passwordS(request):
    if request.method == "GET":
        return render(request, "settings/settings.html")
    return render(request, "settings/settings.html")

def passwordA(request):
    if request.method == "GET":
        return render(request, "settings/settings-acc.html")
    return render(request, "settings/settings-acc.html")