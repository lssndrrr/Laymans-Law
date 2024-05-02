from django.shortcuts import render, redirect
from django.urls import reverse
from authentication.forms import SignUpForm
from .forms import ARegistration
from .models import Abugado, Cases
from django.http import HttpResponse
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


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
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            logger.warning('form is valid')
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            cpassword = form.cleaned_data['password2']
            context['email'] = email
            
            if password == cpassword:
                user.set_password(password)
                user.save()
                
                messages.success(request, f'Account created, {email}. Proceed to registration page.')
                return redirect(reverse('AbugadoSignUp2'), context)
            else:
                form.add_error('cpassword', 'Passwords do not match.')
        else:
            
            logger.warning('form is NOT valid', form)
    else:
        user_type = 'abugado'
        form = SignUpForm(initial={'user_type': user_type})
    context['form'] = form
    return render(request, "abugado/lawyer_signup.html", context)

def signupA2(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = ARegistration()
        context['form'] = form
    return render(request, "abugado/lawyer_signup_cont.html", context)
    
def checkProfile(request):
    pass