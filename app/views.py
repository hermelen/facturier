# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse

from .models import Customer, Product, Quotation
from .forms import QuotationFormSet

# Create your views here.
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


class QuotationDetailView(DetailView):
    model = Quotation


class QuotationCreateView(CreateView):
    model = Quotation
    fields = "__all__"

    def get_context_data(self, **kwargs):
        data = super(QuotationCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['quotationData'] = QuotationFormSet(self.request.POST)
        else:
            data['quotationData'] = QuotationFormSet()
        return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     quotationData = context['quotationData']
    #     with transaction.atomic():
    #         self.object = form.save()
    #
    #         if quotationData.is_valid():
    #             quotationData.instance = self.object
    #             quotationData.save()
    #     return super(QuotationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("quotation-detail")
