from re import L
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MRegistration, MLogin
from .models import Manggagawa, Cases
from authentication.forms import SignUpForm
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

def signupM(request):
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
                user.user_type = 'manggagawa'
                user.save()
                request.session['user_pk'] = user.pk
                print(request.session.get('user_pk'))
                
                messages.success(request, f'Account created, {email}. Proceed to registration page.')
                token = get_random_string(length=32)
                signupM2url = reverse('ManggagawaSignUp2') + f'?from=ManggagawaSignUp&token={token}'
                request.session['token'] = token
                return redirect(signupM2url)
        else:
            try:
                user = CustomUser.objects.get(email=form.data.get('email'), registered=False, user_type='manggagawa')
                password = form.data.get('password1')
                cpassword = form.data.get('password2')
                try:
                    validate_password(password, user=user)
                except ValidationError as e:
                    form.errors['email'].pop()
                    form.add_error('password1', e)
                    return render(request, 'manggagawa/laymen_signup.html', {'form': form})
                if password == cpassword:
                    user.set_password(password)
                    user.save()
                    request.session['user_pk'] = user.pk
                    token = get_random_string(length=32)
                    signupM2url = reverse('ManggagawaSignUp2') + f'?from=ManggagawaSignUp&token={token}'
                    request.session['token'] = token
                    return redirect(signupM2url)
                else:
                    form.errors['email'].pop()
                    form.add_error('password2', 'Passwords do not match.')
            except CustomUser.DoesNotExist:
                logger.warning('form is NOT valid', form)
                print(CustomUser)
    else:
        user_type = 'manggagawa'
        form = SignUpForm()
    context['form'] = form
    return render(request, "manggagawa/laymen_signup.html", context)



def signupM2(request):
    context = {}
    if request.method == "POST":
        form = MRegistration(request.POST)
        if form.is_valid():
            logger.warning('form2 is valid')
            manggagawa = form.save(commit=False)
            user_pk = request.session.get('user_pk')
            if user_pk:
                user = CustomUser.objects.get(pk=user_pk)
                manggagawa.manggagawa_acc = user
                
                user.registered = True
                
                manggagawa.first_name = manggagawa.first_name.title()
                manggagawa.last_name = manggagawa.last_name.title()
                manggagawa.middle_initial = manggagawa.middle_initial.upper()

                manggagawa.save()
                user.manggagawa = manggagawa
                user.save()
                
                del request.session['user_pk']
                return redirect(reverse('ManggagawaLogin'))
            else:
                logger.warning('user_pk does not exist %s', user_pk)
        else:
            logger.warning('form2 is not valid')
            return render(request, "manggagawa/laymen_signup_cont.html", {'form': form})
    elif request.GET.get('from') == 'ManggagawaSignUp' and request.GET.get('token') == request.session.get('token'):
        del request.session['token']
        form = MRegistration()
        context['form'] = form
        return render(request, "manggagawa/laymen_signup_cont.html", context)
    else:
        return redirect(reverse('ManggagawaSignUp'))

def loginM(request):
    context = {}
    if request.method == "POST":
        form = MLogin(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None and user.registered == True:
            
            if user is not None:
                login(request, user)
                if request.user.is_authenticated:
                    print('i go here')
                    manggagawa = request.user.manggagawa
                    # context['roll_number'] = abogado.roll_number
                    # print(context)
                return redirect("MProfile", manggagawa.m_id)
            else:
                form.add_error('password', 'Invalid email or password.') ## to change, check if email is in database and add error/s accordingly
                return render(request, "manggagawa/laymen_login.html", {'form': form})
        else:
            try:
                user = CustomUser.objects.get(email=form.data.get('email'), registered=False)
                password = form.data.get('password')
                if check_password(password, user.password):
                    
                    request.session['user_pk'] = user.pk
                    token = get_random_string(length=32)
                    signupM2url = reverse('ManggagawaSignUp2') + f'?from=ManggagawaSignUp&token={token}'
                    request.session['token'] = token
                    return redirect(signupM2url)
                else:
                    
                    return render(request, 'manggagawa/laymen_login.html', {'form': form})
            except ValidationError as e:
                form.add_error('password', e)
                return render(request, 'manggagawa/laymen_login.html', {'form': form})
        
    else:
        user_type = 'manggagawa'
        form = MLogin(initial={'user_type': user_type})
    context['form'] = form
    return render(request, "manggagawa/laymen_login.html", context)