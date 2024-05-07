from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ARegistration
from .models import Abogado, Cases
from authentication.forms import SignUpForm
from authentication.models import CustomUser, CustomUserManager
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
import logging




logger = logging.getLogger(__name__)


# Create your views here.

def loginA(request):
    if request.method == "POST":
        pass
    if request.method == "GET":
        return render(request, "abogado/lawyer_login.html")
    try:
        password=request.POST.get("password")
        profile=Abogado.objects.get(email_add=request.POST.get("email_add"))
        
        if profile.password == password:
            # return render(request, "abogado/abogado_profile.html", {"profile": profile, })
            pass
        else:
           # return render(request, "abogado/sign_up.html")
            pass
    except:
        # return render(request, "abogado/sign_up.html")
        pass




def signupA(request):
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            logger.warning('form is valid')
            user = form.save(commit=False)
            logger.warning('it happens in save')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            cpassword = form.cleaned_data['password2']
            
            
            if password == cpassword:
                user.set_password(password)
                user.save()
                request.session['user_pk'] = user.pk
                print(request.session.get('user_pk'))
                
                messages.success(request, f'Account created, {email}. Proceed to registration page.')
                token = get_random_string(length=32)
                signupA2url = reverse('AbogadoSignUp2') + f'?from=AbogadoSignUp&token={token}'
                request.session['token'] = token
                return redirect(signupA2url)
        else:
            try:
                user = CustomUser.objects.get(email=form.data.get('email'), registered=False)
                password = form.data.get('password1')
                cpassword = form.data.get('password2')
                try:
                    validate_password(password, user=user)
                except ValidationError as e:
                    form.errors['email'].pop()
                    form.add_error('password1', e)
                    return render(request, 'abogado/lawyer_signup.html', {'form': form})
                if password == cpassword:
                    user.set_password(password)
                    user.save()
                    request.session['user_pk'] = user.pk
                    token = get_random_string(length=32)
                    signupA2url = reverse('AbogadoSignUp2') + f'?from=AbogadoSignUp&token={token}'
                    request.session['token'] = token
                    return redirect(signupA2url)
                else:
                    form.errors['email'].pop()
                    form.add_error('password2', 'Passwords do not match.')
            except CustomUser.DoesNotExist:
                logger.warning('form is NOT valid', form)
    else:
        user_type = 'abogado'
        form = SignUpForm(initial={'user_type': user_type})
    context['form'] = form
    return render(request, "abogado/lawyer_signup.html", context)



def signupA2(request):
    context = {}
    if request.method == "POST":
        form = ARegistration(request.POST)
        if form.is_valid():
            logger.warning('form2 is valid')
            abogado = form.save(commit=False)
            user_pk = request.session.get('user_pk')
            if user_pk:
                user = CustomUser.objects.get(pk=user_pk)
                abogado.abogado_acc = user
                user.registered = True
                abogado.verified = True
                user.save()
                abogado.save()
                del request.session['user_pk']
                return redirect(reverse('AbogadoLogin'))
            else:
                logger.warning('user_pk does not exist %s', user_pk)
        else:
            logger.warning('form2 is not valid')
            return render(request, "abogado/lawyer_signup_cont.html", {'form': form})
    elif request.GET.get('from') == 'AbogadoSignUp' and request.GET.get('token') == request.session.get('token'):
        del request.session['token']
        form = ARegistration()
        context['form'] = form
        return render(request, "abogado/lawyer_signup_cont.html", context)
    else:
        return redirect(reverse('AbogadoSignUp'))
    
def checkProfile(request):
    pass