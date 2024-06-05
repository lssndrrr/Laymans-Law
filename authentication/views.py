from django.shortcuts import render

# Create your views here.
def settingsPA(request):
    if request.method == "GET":
        return render(request, "settings/lawyer_settings-pass.html")
    return render(request, "settings/lawyer_settings-pass.html")

def settingsAA(request):
    if request.method == "GET":
        return render(request, "settings/lawyer_settings-acc.html")
    return render(request, "settings/lawyer_settings-acc.html")

def settingsPM(request):
    if request.method == "GET":
        return render(request, "settings/laymen_settings-pass.html")
    return render(request, "settings/laymen_settings-pass.html")

def settingsAM(request):
    if request.method == "GET":
        return render(request, "settings/laymen_settings-acc.html")
    return render(request, "settings/laymen_settings-acc.html")