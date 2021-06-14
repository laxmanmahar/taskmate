from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def register(request):

    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user created, Log in to started!"))
            return redirect('register')

    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})


def logout(request):
    auth.logout(request)
    return redirect('index')
