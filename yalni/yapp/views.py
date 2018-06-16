# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from django.db import IntegrityError
from .models import Motherboard
from .forms import MotherboardForm

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
def ipc(request):
	if request.method == 'POST':
		form = MotherboardForm(request.POST)
		if form.is_valid():
			obj = Motherboard()
			obj.motherboard_part_no = form.cleaned_data['motherboard_part_no']
			obj.supported_processor = form.cleaned_data['supported_processor']
			obj.number_of_mem_slot = form.cleaned_data['number_of_mem_slot'] 
			obj.save()
			return render(request, 'ipc.html')
			
		else:
			form = MotherboardForm( )
									     
	return render(request, 'ipc.html')






