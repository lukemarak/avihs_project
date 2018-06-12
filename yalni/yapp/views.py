# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def ipc510(request):
    return render(request, 'ipc510.html')

@login_required
def ipc610(request):
    return render(request, 'ipc610.html')

@login_required
def acp4000(request):
    return render(request, 'acp4000.html')

@login_required
def acp4360(request):
    return render(request, 'acp4360.html')

@login_required
def acp2000(request):
    return render(request, 'acp2000.html')
