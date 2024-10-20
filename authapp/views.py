from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm


def login(request):
    title = 'Вход'

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        login_form = ShopUserLoginForm()

    context = {
        'title': title,
        'login_form': login_form,
    }

    return render(request, 'authapp/login.html', context)


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))