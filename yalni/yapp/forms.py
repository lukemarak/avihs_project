from django import forms
from .models import Client, Chasis, Motherboard, Configuration, Detail

class ClientForm(forms.Form):
	client = forms.CharField(max_length=100)
	client_address = forms.CharField(max_length=200)
	client_address_short = forms.CharField(max_length=100)
	client_nick_name = forms.CharField(max_length=100)
		

class ChasisForm(forms.Form):
	chasis = forms.CharField(max_length=20)
	with_or_without_bay = forms.CharField()
	
class MotherboardForm(forms.Form):
	motherboard_part_no = forms.CharField(max_length=50)
	supported_processor = forms.CharField(max_length=200)
	BAY = (
		('', '----Select Option----'),
		('No', 'Without Bay'),
		('Two', 'With 2 Bays'),
		('Four', 'With 4 Bays'),
		('Six', 'With 6 Bays'),
	)
	number_of_mem_slot = forms.CharField(max_length=50, widget=forms.Select(choices=BAY))

