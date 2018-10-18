# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt #decorator
from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator #decorator
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile
# from django.urllib2 import request
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet

from .forms import ProductListForm
from .models import Customer, Product, Quotation, ProductList, quotationStatus

import urllib


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


@method_decorator(csrf_exempt, name = 'dispatch')
class QuotationDetailView(DetailView):
    model = Quotation

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        context["products"] = Product.objects.all()
        context["product_list_form"] = ProductListForm(initial={"quotation" : self.get_object()})
        return context


class QuotationListView(ListView):
    model = Quotation

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context["choices"] = quotationStatus
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
    template_name = "app/quotation_pdf.html"

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        lines = self.get_object().productlist_set.all()
        sum = 0
        for line in lines:
            subsum = line.product.price * line.quantity
            sum += subsum
        context['sum'] = sum
        return context

def generate_pdf(request, slug):
    quotation = Quotation.objects.get(slug=slug)
    # Rendered
    html_string = render_to_string('app/quotation_pdf.html', {'quotation': quotation})
    html = HTML(string=html_string)
    result = html.write_pdf()
    # html = HTML('http://127.0.0.1:8000/quotation/ap-web-design-2/').write_pdf('/tmp/weasyprint-website.pdf',
    # stylesheets=[CSS(string='body {font-family: serif !important; }')])

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=quotation.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())

    return response


    # return reverse("index")



    # template_name = 'app/quotation_pdf.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = DetailView.get_context_data(self, *args, **kwargs)
    #     lines = self.get_object().productlist_set.all()
    #     sum = 0
    #     for line in lines:
    #         subsum = line.product.price * line.quantity
    #         sum += subsum
    #     context['sum'] = sum
    #     return context






@method_decorator(csrf_exempt, name = 'dispatch')#empeche la validation csrf token
class ProductListUpdateView(View):

    def post(self, request, id, field):
        productlist = ProductList.objects.get(pk=id)
        setattr(productlist,field,request.POST.get("value"))
        productlist.save()
        return HttpResponse({'success' :True})


@method_decorator(csrf_exempt, name = 'dispatch')
class ProductListDeleteView(View):

    def post(self, request, id):
        productlist = ProductList.objects.get(id=id)
        productlist.delete()
        return HttpResponse({'success' :True})


# @method_decorator(csrf_exempt, name = 'dispatch')
class ProductListCreateView(CreateView):
    model = ProductList
    form_class = ProductListForm


    def post(self, request, **kwargs):
        CreateView.post(self, request, kwargs)
        return JsonResponse({
            "editable_data_url" : reverse("productlist-update", args=[self.object.id, 'quantity']),
            "del_button_data_url" : reverse("productlist-delete", args=[self.object.id]),
            "productName" : self.object.product.name,
            "quantity" : self.object.quantity,
            "price" : self.object.product.price,
            "id": self.object.id
        })

    def get_success_url(self):
        return reverse("quotation-detail", args=[self.object.quotation.slug])


    # def post(self, request, id):
    #     if(request.POST):
    #
    #         productlist_data = request.POST.dict()
    #         product = request.POST.get("product")
    #         quantity = request.POST.get("quantity")
    #         quotation = id
    #         n = ProductList(product = product, quantity=quantity,quotation=quotation)
    #         n.save()
    #         return HttpResponse({'success' :True})
        # quotation = Quotation.objects.get(pk=id)
        # setattr(productlist,"product",request.POST.get("value"))
        # productlist.save()
        # return HttpResponse({'success' :True})
