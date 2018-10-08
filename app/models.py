# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
# from django.contrib.gis.db import models


class Customer(models.Model):
    first_name   = models.CharField(max_length=100, verbose_name="Prénom", null=True, blank=True)
    last_name    = models.CharField(max_length=100, verbose_name="Nom", null=True, blank=True)
    slug         = AutoSlugField(populate_from='full_name', verbose_name="Slug", null=True, blank=True, unique=True)
    company      = models.CharField(max_length=100, verbose_name="Entreprise", null=True, blank=True)
    phone_number = models.CharField(max_length=12, verbose_name="Téléphone", null=True, blank=True)
    email        = models.EmailField(max_length=200, verbose_name="E-mail", null=True, blank=True)
    address      = models.CharField(max_length=150, verbose_name="Adresse", null=True, blank=True)
    zipcode      = models.CharField(max_length=10, verbose_name="Code Postal", null=True, blank=True)
    city         = models.CharField(max_length=50, verbose_name="Ville", null=True, blank=True)

    def full_name(self):
        return "%s %s %s" %(self.company, self.first_name, self.last_name)

    def __unicode__(self):
        return self.last_name


class Product(models.Model):
    name        = models.CharField(max_length=100, verbose_name="Nom", null=True, blank=True)
    slug        = AutoSlugField(populate_from='full_name', verbose_name="Slug", null=True, blank=True, unique=True)
    ref         = models.CharField(max_length=150, verbose_name="Référence", null=True, blank=True)
    short_desc  = models.TextField(verbose_name="En bref", null=True, blank=True)
    decription  = models.TextField(verbose_name="Description", null=True, blank=True)
    price       = models.FloatField(verbose_name="Price", null=True, blank=True) #floatfield

    def full_name(self):
        return "%s %s" %(self.name, self.ref)

    def __unicode__(self):
        return self.name

quotationStatus = [
    (1, "devis en cours"),
    (2, "devis annulé"),
    (3, "facture"),
]

class Quotation(models.Model):
    customer  = models.ForeignKey(Customer,on_delete=models.CASCADE)
    reference = models.IntegerField(verbose_name="Référence")
    status    = models.IntegerField(choices=quotationStatus, null=True, blank=True)

    def __unicode__(self):
        return str(self.reference)


class ProductList(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Quantité")
    quotation = models.ForeignKey(Quotation,on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.quotation.reference)
