from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Loginform


def homepage(request):
    return render(request, 'accounts/homepage.html')

def logout_user(request):
    logout(request)
    return redirect('/login')

def login_user(request):
    context = {
        'form_login': Loginform,
        'activate_login': 'activate'
    }
    return render(request, 'accounts/login.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registration Successful')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to Register')
            return render('accounts/register.html', {'from_register': form})

    context = {
        'form_register': UserCreationForm,
        'activate_register': 'activate'
    }
    return render(request, 'accounts/register.html', context)


