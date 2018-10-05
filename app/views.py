# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse

from .models import Customer

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
