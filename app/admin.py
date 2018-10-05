# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, Product, Quotation

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','slug', 'company', 'phone_number', 'email', 'address', 'zipcode', 'city')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','ref','short_desc', 'decription', 'price')


class QuotationAdmin(admin.ModelAdmin):
    list_display = ('customer','reference', 'status')


# Register your models here.

#configurer pour consulter models dans admin
#productlist doit être inliné dans quotation admin
