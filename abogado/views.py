from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ARegistration, ALogin
from .models import Abogado, Cases
from authentication.forms import DeleteAccForm, SignUpForm, ChangePWForm, DeleteAccForm
from authentication.models import CustomUser, CustomUserManager
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
import logging
from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password






logger = logging.getLogger(__name__)


# Create your views here.


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
                user.user_type = 'abogado'
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
                user = CustomUser.objects.get(email=form.data.get('email'), registered=False, user_type='abogado')
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
                print(CustomUser)
    else:
        user_type = 'abogado'
        form = SignUpForm()
        form = SignUpForm(initial={'user_type': user_type})
    context['form'] = form
    return render(request, "abogado/lawyer_signup2.html", context)



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
                
                abogado.first_name = abogado.first_name.title()
                abogado.last_name = abogado.last_name.title()
                abogado.middle_initial = abogado.middle_initial.upper()

                abogado.save()
                user.abogado = abogado
                user.save()
                
                del request.session['user_pk']
                return redirect(reverse('AbogadoLogin'))
            else:
                logger.warning('user_pk does not exist %s', user_pk)
        else:
            logger.warning('form2 is not valid')
            return render(request, "abogado/lawyer_signup_cont.html", {'form': form})
    elif (request.GET.get('from') == 'AbogadoSignUp' or request.GET.get('from') == 'AbogadoLogIn') and request.GET.get('token') == request.session.get('token'):
        del request.session['token']
        form = ARegistration()
        context['form'] = form
        return render(request, "abogado/lawyer_signup_cont.html", context)
    else:
        return redirect(reverse('AbogadoSignUp'))
    

def loginA(request):
    context = {}
    if request.method == "POST":
        form = ALogin(request.POST)

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is None:
            if not CustomUser.objects.filter(email=email).exists():
                form.add_error('email', 'User with this email does not exist.')
            else:
                form.errors.clear()
                form.add_error('password', 'Invalid email or password.')
            return render(request, 'abogado/lawyer_login.html', {'form': form})
            
        elif user is not None and user.registered == True:
            login(request, user)
            if request.user.is_authenticated:
                abogado = request.user.abogado
                # context['roll_number'] = abogado.roll_number
                # print(context)
            return redirect("AProfile", abogado.roll_number)
            
        elif user is not None and user.registered == False:
            try:
                user = CustomUser.objects.get(email=form.data.get('email'), registered=False)
                password = form.data.get('password')
                if check_password(password, user.password):
                    
                    request.session['user_pk'] = user.pk
                    token = get_random_string(length=32)
                    signupA2url = reverse('AbogadoSignUp2') + f'?from=AbogadoLogIn&token={token}'
                    request.session['token'] = token
                    return redirect(signupA2url)
                else:
                    
                    return render(request, 'abogado/lawyer_login.html', {'form': form})
            except ValidationError as e:
                form.add_error('password', e)
                return render(request, 'abogado/lawyer_login.html', {'form': form})
    else:
        user_type = 'abogado'
        form = ALogin(initial={'user_type': user_type})
    context['form'] = form
    return render(request, "abogado/lawyer_login.html", context)




    
@login_required
def ProfileA(request, roll_number):
    context = {}
    if request.method == "GET":
        return render(request, "abogado/lawyer_homepage-obs.html", context)

@login_required
def Wiki(request):
    pass

@login_required
def ASettings(request, roll_number):
    context = {}
    if request.method == "POST":
        pwform = ChangePWForm(request.POST)
        delform = DeleteAccForm(request.POST)
        if pwform.is_valid():
            if not authenticate(email=request.user.email, password=request.POST['current_password']):
                print('WEH')
                pwform.add_error("current_password", "Current password is incorrect.")
            else:
                if request.POST['new_password1'] == request.POST['new_password2']:
                    request.user.set_password(request.POST['new_password1'])
                    print("changed")
                    request.user.save()
                else:
                    raise pwform.ValidationError("Passwords do not match.")
            return redirect(reverse('AbogadoLogin'))
        elif delform.is_valid():
            if not authenticate(email=request.user.email, password=request.POST['current_password']):
                print('WEH')
                delform.add_error("current_password", "Password is incorrect.")
            elif not request.POST['confirm']:
                delform.add_error("confirm", "Before proceeding, please confirm that you understand the consequences of this action.")
            elif authenticate(email=request.user.email, password=request.POST['current_password']) and request.POST['confirm']:
                request.user.delete()
                return redirect(reverse('AbogadoLogin'))
            print("User deleted successfully")
            return render(request, "settings/lawyer_settings-pass.html", {'pwform': pwform, 'delform': delform})
            
        
    else:
        pwform = ChangePWForm()
        delform = DeleteAccForm()
        context['pwform'] = pwform
        context['delform'] = delform
        return render(request, "settings/lawyer_settings-pass.html", context)
    

@login_required
def Browse(request, roll_number):
    context = {}
    return render(request, 'abogado/lawyer_browsecase.html', context)

@login_required
def Logout(request):
    logout(request)
    return redirect(reverse('AbogadoLogin'))
