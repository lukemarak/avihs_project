from django import forms
from .models import Configuration
from django.db import models

class ConfigurationForm(forms.ModelForm):
	class Meta:
		model = Configuration
		fields = ('client','chasis','motherboard_part_no','processor','memory','hard_drive','smps','dvd_drive','operating_system','inclusive_part','created','save_as',)
		
		def __init__(self, user, *args, **kwargs):
			super(ConfigurationForm, self).__init__(*args, **kwargs)
			self.fields['client','chasis','motherboard_part_no'].queryset = Category.objects.filter(user=user)


