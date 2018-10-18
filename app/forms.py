# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import ProductList, Quotation
#
#
# class QuotationForm(ModelForm):
#     class Meta:
#         model = Quotation
#         exclude = ()
#
# QuotationFormSet = inlineformset_factory(Quotation, ProductList, form=QuotationForm, extra=1)


class ProductListForm(ModelForm):
    class Meta:
        model = ProductList
        fields = "__all__"
