import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

# Create your views here.
from django.utils import timezone

from authorization.forms import RegisterForm, LoginForm, VerifyForm
from authorization.models import EmailAuth


def homepage(request):
    context = {

    }
    return render(request, 'index.html', context)


def register_page(request):
    register_form = RegisterForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')
    elif register_form.is_valid():
        verify_form = VerifyForm()
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        rand_num = random.randint(111111, 999999)
        EmailAuth.objects.create(username=username, email=email, num=rand_num)
        # internet connection checker
        url = 'https://www.google.com'
        timeout = 3
        result = ''
        try:
            requests.get(url, timeout=timeout)
            result = 'True'
        except (requests.ConnectionError or requests.Timeout) as exception:
            result = 'False'
        if result == 'False':
            return HttpResponse('no internet connection')
        else:
            send_mail('verification code',
                      f'Verification code \n {rand_num} \n\nif its not You, just do Nothing',
                      'testingappdjango@gmail.com', [f'{email}'], fail_silently=False)
        # end internet connection checker

        return render(request, 'emailverify.html',
                      {'verify_form': verify_form, 'username': username, 'email': email, 'password': password})
    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        authenticate_check = authenticate(username=username, password=password)
        if authenticate_check:
            login(request, authenticate_check)
            return redirect('/')
    elif request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm()

    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')


def activate(request):
    verify_form = VerifyForm(request.POST or None)
    if verify_form.is_valid():
        code = verify_form.cleaned_data['code']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        search = EmailAuth.objects.filter(num__exact=code).exists()
        print(search)
        if search:
            print(f'{username},{email},{password}')
            found: EmailAuth = EmailAuth.objects.filter(num__exact=code).first()
            c_minute = found.created_time.minute
            n_minute = timezone.now().minute
            if not 0 <= (int(n_minute) - int(c_minute)) <= 1:
                found.delete()
                return HttpResponse('code is unusable anymore')
            found.delete()
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('/login')
        return HttpResponse('Something is wrong ,please try again')
    return HttpResponse('Something is wrong ,please try again.')
