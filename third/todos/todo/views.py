from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import InternalError


def home(request):
    return render(request, 'todo/home.html')


def singnupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/singnupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('curenttodos')
            except InternalError:
                return render(request, 'todo/singnupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует. Задайте другое'
                })
        else:
            return render(request, 'todo/singnupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'
            })


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return redirect(request, 'todo/loginuser.html', {
                'form': AuthenticationForm,
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('curenttodos')

def curenttodos(request):
    return render(request, 'todo/curenttodos.html')
