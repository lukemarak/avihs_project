# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Client, Chasiz, Motherboard, Configuration, Detail

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['client','client_address','client_address_short','client_nick_name']
    prepopulated_fields = {'client_nick_name': ('client','client_address',)}
admin.site.register(Client, ClientAdmin)

class ChasizAdmin(admin.ModelAdmin):
    list_display = ('chasis', 'with_or_without_bay',)
admin.site.register(Chasiz, ChasizAdmin)

class MotherboardAdmin(admin.ModelAdmin):
    list_display = ['motherboard_part_no','supported_processor','number_of_mem_slot']
admin.site.register(Motherboard, MotherboardAdmin)

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['client','chasis','motherboard_part_no','processor','memory','hard_drive','smps','dvd_drive','operating_system','inclusive_part','created','save_as']
admin.site.register(Configuration, ConfigurationAdmin)

class DetailAdmin(admin.ModelAdmin):
    list_display=['save_as','chasis','motherboard','memory','hard_drive','smps','dvd_drive','product_key','extra','quantity','assembled_on','assembled_by']
    search_fields = ['chasis', 'motherboard','memory','hard_drive','product_key']
    list_filter = ['save_as']
admin.site.register(Detail, DetailAdmin)
