from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from mainapp.views import get_menu_links


def login(request):
    title = 'Вход'

    _next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)

                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])

                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        login_form = ShopUserLoginForm()

    context = {
        'title': title,
        'login_form': login_form,
        'menu_links': get_menu_links(),
        'next': _next,
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
        'menu_links': get_menu_links(),
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    title = ' Редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'title': title,
        'edit_form': edit_form,
        'menu_links': get_menu_links(),
    }

    return render(request, 'authapp/edit.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))