# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse
# from django.urllib2 import request

from .models import Customer, Product, Quotation, ProductList
# from .forms import QuotationFormSet

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet

class IndexView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)


class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'

    def get_success_url(self):
        return reverse("customer-detail", args=[self.object.slug])

class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse("customer-detail", args=[self.object.slug])


class CustomerDeleteView(DeleteView):
    model = Customer

    def get_success_url(self):
        return reverse("customers-list")


class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Customer.objects.filter(company__icontains = q)
            return queryset
        else:
            return Customer.objects.all()


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

    def get_success_url(self):
        return reverse("product-detail", args=[self.object.slug])


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Product.objects.filter(name__icontains = q)
            return queryset
        else:
            return Product.objects.all()

class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse("product-detail", args=[self.object.slug])


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse("products-list")


class ProductListInline(InlineFormSet):
    model = ProductList
    fields = "__all__"


class QuotationCreateView(CreateWithInlinesView):
    model = Quotation
    inlines = [ProductListInline,]
    fields = "__all__"
    template_name = 'app/quotation_form.html'
    success_url = '/'

    def get_success_url(self):
        return reverse("quotation-detail", args=[self.object.slug])


class QuotationDetailView(DetailView):
    model = Quotation

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        lines = self.get_object().productlist_set.all()
        sum = 0
        for line in lines:
            subsum = line.product.price * line.quantity
            sum += subsum
        context['sum'] = sum
        return context


class QuotationListView(ListView):
    model = Quotation

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context["choices"] = [
            (1, "devis en cours"),
            (2, "devis annulé"),
            (3, "facture en attente"),
            (4, "facture à relancer"),
            (5, "facture réglée"),
        ]
        return context

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Quotation.objects.filter(status = q)
            return queryset
        else:
            return Quotation.objects.all()


class QuotationPdfDetailView(DetailView):
    model = Quotation
    template_name = 'app/quotation_pdf.html'
    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        lines = self.get_object().productlist_set.all()
        sum = 0
        for line in lines:
            subsum = line.product.price * line.quantity
            sum += subsum
        context['sum'] = sum
        return context
