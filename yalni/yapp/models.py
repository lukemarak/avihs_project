# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    client = models.CharField(max_length=50)
    client_address = models.CharField(max_length=255)
    client_address_short = models.CharField(max_length=20)
    client_nick_name = models.SlugField(max_length=100)

    def __str__(self):
        return self.client_nick_name

    class Meta:
        ordering = ['client', 'client_address']

class Chasis(models.Model):
    chasis = models.CharField(max_length=100)
    WITH_BAY = (
        ('','----Select Option----'),
        ('No','Without Bay'),
        ('Two','With Two HDD Bay'),
        ('Four','With Four HDD Bay'),
        ('Six','With Six HDD Bay'),
    )
    with_or_without_bay = models.CharField(max_length=20, choices=WITH_BAY)

    def __str__(self):
        return self.chasis

class Motherboard(models.Model):
    motherboard_part_no = models.CharField(max_length=50)
    supported_processor = models.CharField(max_length=200)
    number_of_mem_slot = models.PositiveIntegerField()

    def __str__(self):
        return self.motherboard_part_no

    class Meta:
        ordering = ['motherboard_part_no', 'supported_processor', 'number_of_mem_slot']

class Configuration(models.Model):
    client = models.ForeignKey(Client, related_name='configurations')
    chasis = models.ForeignKey(Chasis, related_name='configurations')
    motherboard_part_no = models.ForeignKey(Motherboard, related_name='configurations')
    processor = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    hard_drive = models.CharField(max_length=100)
    smps = models.CharField(max_length=100)
    dvd_drive = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    inclusive_part = models.CharField(max_length=200)
    created = models.DateField('created')
    save_as = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.save_as

    class Meta:
        ordering = ['client','chasis','motherboard_part_no','processor','memory','hard_drive','smps','operating_system','inclusive_part','created','save_as']
        verbose_name = 'configuration'
        verbose_name_plural = 'configurations'

        def __str__(self):
            return self.save_as

class Detail(models.Model):
    save_as = models.ForeignKey(Configuration, related_name='details')
    chasis = models.CharField(max_length=20, blank=True)
    motherboard = models.CharField(max_length=20, blank=True)
    memory = models.CharField(max_length=200, blank=True)
    hard_drive = models.CharField(max_length=200, blank=True)
    smps = models.CharField(max_length=50, blank=True)
    dvd_drive = models.CharField(max_length=40, blank=True)
    product_key = models.CharField(max_length=100, blank=True)
    extra = models.CharField(max_length=200, blank=True)
    quantity = models.PositiveIntegerField()
    assembled_on = models.DateField('date')
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
    assembled_by = models.CharField(max_length=20, choices=ASSEMBLED_BY)

    class Meta:
        verbose_name = 'detail'
        verbose_name_plural = 'details'
        unique_together = ('chasis','motherboard','memory','hard_drive','smps','dvd_drive','product_key',)

        def __str__(self):
            return self.chasis
