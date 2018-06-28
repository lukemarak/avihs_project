# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from django.db import IntegrityError
from django.views import View
from django.http import HttpResponse
from .models import Client, Chasiz, Motherboard, Configuration, Detail
from .forms import MotherboardForm, ClientForm, ChasizForm, ConfigurationForm, DetailForm

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
def board(request):
	if request.method == 'POST':
		form = MotherboardForm(request.POST)
		if form.is_valid():
			obj = Motherboard()
			obj.motherboard_part_no = form.cleaned_data['motherboard_part_no']
			obj.supported_processor = form.cleaned_data['supported_processor']
			obj.number_of_mem_slot = form.cleaned_data['number_of_mem_slot']
			obj.save()
			return render(request, 'board.html')

		else:
			form = MotherboardForm( )

	return render(request, 'board.html')

@login_required
def add_client(request):
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			obj = Client()
			obj.client = form.cleaned_data['client']
			obj.client_address = form.cleaned_data['client_address']
			obj.client_address_short = form.cleaned_data['client_address_short']
			obj.client_nick_name = form.cleaned_data['client_nick_name']
			obj.save()
			return render(request, 'add_client.html')

		else:
			form = ClientForm()
	return render(request, 'add_client.html')

@login_required
def add_chasis(request):
	if request.method == 'POST':
		form = ChasizForm(request.POST)
		if form.is_valid():
			obj = Chasiz()
			obj.chasis = form.cleaned_data['chasis']
			obj.with_or_without_bay = form.cleaned_data['with_or_without_bay']
			obj.save()
			return render(request, 'add_chasis.html')
		else:
			form = ChasizForm()

	return render(request, 'add_chasis.html')

@login_required
def create_config(request):
	if request.method == 'POST':
		form = ConfigurationForm(request.POST)
		if form.is_valid():
			obj = Configuration()
			obj.client = form.cleaned_data['client']
			obj.chasis = form.cleaned_data['chasis']
			obj.motherboard_part_no = form.cleaned_data['motherboard_part_no']
			obj.processor = form.cleaned_data['processor']
			obj.memory = form.cleaned_data['memory']
			obj.hard_drive = form.cleaned_data['hard_drive']
			obj.smps = form.cleaned_data['smps']
			obj.dvd_drive = form.cleaned_data['dvd_drive']
			obj.operating_system = form.cleaned_data['operating_system']
			obj.inclusive_part = form.cleaned_data['inclusive_part']
			obj.created = form.cleaned_data['created']
			obj.save_as = form.cleaned_data['save_as']
			obj.save()
			return render(request, 'create_config.html')
		else:
			form = ConfigurationForm()

	return render(request, 'create_config.html')

@login_required
def detail(request):
	if request.method == 'POST':
		form = DetailForm(request.POST)
		if form.is_valid():
			obj = Detail()
			obj.save_as = form.cleaned_data['save_as']
			obj.chasis = form.cleaned_data['chasis']
			obj.motherboard = form.cleaned_data['memory']
			obj.hard_drive = form.cleaned_data['hard_drive']
			obj.smps = form.cleaned_data['smps']
			obj.dvd_drive = form.cleaned_data['dvd_drive']
			obj.product_key = form.cleaned_data['product_key']
			obj.extra = form.cleaned_data['extra']
			obj.quantity = form.cleaned_data['quantity']
			obj.assembled_on = form.cleaned_data['assembled_on']
			obj.assembled_by = form.cleaned_data['assembled_by']
			obj.save()
			return render(request, 'detail.html')

		else:
			form = DetailForm()

	return render(request, 'detail.html')
