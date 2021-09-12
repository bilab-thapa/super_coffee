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
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user credentials")
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': Loginform,
        'activate_login': 'active'
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
            return redirect('/register')
            #return render(request, 'accounts/register.html', {'from_register': form})

    context = {
        'form_register': UserCreationForm,
        'activate_register': 'active'
    }
    return render(request, 'accounts/register.html', context)

