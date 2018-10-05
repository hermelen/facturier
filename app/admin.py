# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, Product, Quotation, ProductList

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','slug', 'company', 'phone_number', 'email', 'address', 'zipcode', 'city')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','ref','short_desc', 'decription', 'price')


class ProductListInline(admin.TabularInline):
    model = ProductList


class QuotationAdmin(admin.ModelAdmin):
    inlines = [
        ProductListInline,
    ]
    list_display = ('customer','reference', 'status')




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Quotation, QuotationAdmin)
