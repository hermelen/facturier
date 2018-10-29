# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

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
# from django.core.mail import send_mail
from django.core.mail import EmailMessage

from .forms import ProductListForm
from .models import Customer, Product, Quotation, ProductList
from .models import quotationStatus, allStatus, billStatus
from django.db.models import Q

from django.apps import apps

from facturier.extra_settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

import urllib


class IndexView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)


class CustomerCreateView(PermissionRequiredMixin,CreateView):
    model = Customer
    fields = '__all__'
    permission_required = 'app.add_customer'

    def get_success_url(self):
        return reverse("customer-detail", args=[self.object.slug])


class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Customer.objects.filter(company__icontains = q)
            return queryset
        else:
            return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Customer
    fields = "__all__"
    permission_required = 'app.change_customer'

    def get_success_url(self):
        return reverse("customer-detail", args=[self.object.slug])


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    permission_required = 'app.delete_customer'


    def get_success_url(self):
        return reverse("customers-list")


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    permission_required = 'app.add_product'

    def get_success_url(self):
        return reverse("product-detail", args=[self.object.slug])


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Product.objects.filter(name__icontains = q)
            return queryset
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    permission_required = 'app.change_product'


    def get_success_url(self):
        return reverse("product-detail", args=[self.object.slug])


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'app.delete_product'


    def get_success_url(self):
        return reverse("products-list")


class ProductListInline(InlineFormSet):
    model = ProductList
    fields = "__all__"


@method_decorator(csrf_exempt, name = 'dispatch')#empeche la validation csrf token
class ProductListUpdateView(PermissionRequiredMixin, View):
        permission_required = 'app.change_productlist'

        def post(self, request, id, field):
            productlist = ProductList.objects.get(pk=id)
            setattr(productlist,field,request.POST.get("value"))
            productlist.save()
            return HttpResponse({'success' :True})


class QuotationCreateView(PermissionRequiredMixin, CreateWithInlinesView):
    model = Quotation
    inlines = [ProductListInline,]
    fields = "__all__"
    template_name = 'app/quotation_form.html'
    success_url = '/'
    permission_required = 'app.add_product'


    def get_success_url(self):
        return reverse("quotation-detail", args=[self.object.slug])


class QuotationListView(ListView):
    quotation = Quotation.objects.filter(Q(status=1) | Q(status=2))


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
            return Quotation.objects.filter(Q(status=1) | Q(status=2))


@method_decorator(csrf_exempt, name = 'dispatch')
class QuotationDetailView(DetailView):
    model = Quotation

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        context["products"] = Product.objects.all()
        context["product_list_form"] = ProductListForm(initial={"quotation" : self.get_object()})
        context["all_status"] = allStatus
        return context


@method_decorator(csrf_exempt, name = 'dispatch')
class QuotationUpdateView(PermissionRequiredMixin,View):
            permission_required = 'app.change_quotation'

            def post(self, request, id, field):
                quotation = Quotation.objects.get(pk=id)
                setattr(quotation,field,request.POST.get("value"))
                quotation.save()
                return HttpResponse({'success' :True})


class BillListView(ListView):
    bill = Quotation.objects.filter(Q(status=3) | Q(status=4) | Q(status=5))


    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context["choices"] = billStatus
        return context

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Quotation.objects.filter(status = q)
            return queryset
        else:
            return Quotation.objects.filter(Q(status=3) | Q(status=4) | Q(status=5))


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
    customerMail = quotation.customer.email
    customerName = quotation.customer.first_name.capitalize() +' '+ quotation.customer.last_name.capitalize()

    lines = quotation.productlist_set.all()
    sum = 0
    for line in lines:
        subsum = line.product.price * line.quantity
        sum += subsum

    status = quotation.status
    if status < 3:
        status = 'devis'
    else:
        status = 'facture'

    html_string = render_to_string('app/quotation_pdf.html', {'quotation': quotation, 'sum': sum})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename='+status+'-'+slug+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    url = reverse('quotation-pdf', args=[slug] )
    pdf = HTML(string=html_string, base_url=url).write_pdf()

    email = EmailMessage(
        status.capitalize() + ': ' + quotation.slug,
        'Hi '+ customerName +', please find in attachment your ' + status,
        EMAIL_HOST_USER,
        [customerMail],
        [EMAIL_HOST_USER],
        reply_to=['another@example.com'],
        headers={'Message-ID': 'foo'},
    )
    email.attach(status+'-'+slug+'.pdf', pdf, "application/pdf")
    email.send()

    return HttpResponse(pdf, content_type='application/pdf')









@method_decorator(csrf_exempt, name = 'dispatch')
class ProductListDeleteView(PermissionRequiredMixin, View):
    permission_required = 'app.delete_productlist'

    def post(self, request, id):
        productlist = ProductList.objects.get(id=id)
        productlist.delete()
        return HttpResponse({'success' :True})


# @method_decorator(csrf_exempt, name = 'dispatch')
class ProductListCreateView(PermissionRequiredMixin, CreateView):
    model = ProductList
    form_class = ProductListForm
    permission_required = 'app.add_productlist'


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



# def generate_pdf(request, slug):
#     quotation = Quotation.objects.get(slug=slug)
#     customerMail = quotation.customer.email
#     customerName = quotation.customer.first_name
#
#     status = quotation.status
#     if status < 3:
#         status = 'devis'
#     else:
#         status = 'facture'
#     html_string = render_to_string('app/quotation_pdf.html', {'quotation': quotation})
#     html = HTML(string=html_string)
#     app_path = apps.get_app_config('app').path
#     result = html.write_pdf()
#
#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=quotation.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'r')
#         response.write(output.read())
#     html.write_pdf(app_path+'/media/'+status+'-'+slug+'.pdf')
#
#     email = EmailMessage(
#         'Hello '+customerName,
#         'Please find in attachment your ' + status,
#         EMAIL_HOST_USER,
#         [customerMail],
#         [EMAIL_HOST_USER],
#         reply_to=['another@example.com'],
#         headers={'Message-ID': 'foo'},
#     )
#     email.attach(app_path+'/media/'+status+'-'+slug+'.pdf', 'img_data', 'image/pdf')
#     email.send()
#
#     return response
#
#
#     return reverse("index")
#
#
#
#     template_name = 'app/quotation_pdf.html'
#     def get_context_data(self, *args, **kwargs):
#         context = DetailView.get_context_data(self, *args, **kwargs)
#         lines = self.get_object().productlist_set.all()
#         sum = 0
#         for line in lines:
#             subsum = line.product.price * line.quantity
#             sum += subsum
#         context['sum'] = sum
#         return context
