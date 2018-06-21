from django import forms
from .models import Client, Chasiz, Motherboard, Configuration, Detail
from django.db import models

class ClientForm(forms.Form):
	client = forms.CharField(max_length=100)
	client_address = forms.CharField(max_length=200)
	client_address_short = forms.CharField(max_length=100)
	client_nick_name = forms.CharField(max_length=100)


class ChasizForm(forms.Form):
	chasis = forms.CharField(max_length=20)
	BAY = (
		('', '----Select Option----'),
		('No', 'Without Bay'),
		('Two', 'With 2 Bays'),
		('Four', 'With 4 Bays'),
		('Six', 'With 6 Bays'),
	)
	with_or_without_bay = forms.CharField(max_length=50, widget=forms.Select(choices=BAY))

class MotherboardForm(forms.Form):
	motherboard_part_no = forms.CharField(max_length=50)
	supported_processor = forms.CharField(max_length=200)
	number_of_mem_slot = forms.IntegerField()

class ConfigurationForm(forms.Form):
	client = forms.ModelChoiceField(queryset=Client.objects.all() , required=True)
	chasis = forms.ModelChoiceField(queryset=Chasiz.objects.all() , required=True)
	motherboard_part_no = forms.ModelChoiceField(queryset=Motherboard.objects.all() , required=True)
	processor = forms.CharField(max_length=100)
	memory = forms.CharField(max_length=100)
	hard_drive = forms.CharField(max_length=100)
	smps = forms.CharField(max_length=100)
	dvd_drive = forms.CharField(max_length=100)
	operating_system = forms.CharField(max_length=100)
	inclusive_part = forms.CharField(max_length=200)
	created = forms.DateField()
	save_as = forms.CharField(max_length=50)

class DetailForm(forms.Form):
	save_as = forms.ModelChoiceField(queryset=Configuration.objects.all(), initial=0 , required=True)
	chasis = forms.CharField(max_length=20)
	motherboard = forms.CharField(max_length=20)
	memory = forms.CharField(max_length=200)
	hard_drive = forms.CharField(max_length=200)
	smps = forms.CharField(max_length=50)
	dvd_drive = forms.CharField(max_length=40)
	product_key = forms.CharField(max_length=100)
	extra = forms.CharField(max_length=200)
	quantity = forms.IntegerField()
	assembled_on = forms.DateField()
	ASSEMBLED_BY = (
		('','----Select a person----'),
		('Luke', 'Luke Marak'),
		('Balaji', 'Balaji'),
		('Gopala','Gopalakhrishnan'),
		('Mukesh', 'Mukesh Gautam'),
		('Venkey', 'R.Venkatesh'),
		('Manikndn', 'Manikandan'),
		('Santosh', 'Santosh'),
		('Others','Someone'),
	)

	assembled_by = forms.CharField(max_length=50, widget=forms.Select(choices=ASSEMBLED_BY))
