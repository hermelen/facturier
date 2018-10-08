"""facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


from app.views import IndexView, CustomerCreateView, CustomerDetailView, CustomerUpdateView, CustomerDeleteView, CustomerListView
from app.views import ProductCreateView, ProductDetailView, ProductUpdateView,ProductListView, ProductDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    url(r'^customers/', CustomerListView.as_view(), name='customers-list'),
    url(r'^customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    url(r'^customer/(?P<slug>[-\w]+)/delete/$', CustomerDeleteView.as_view(), name="customer-delete"),
    url(r'^customer/(?P<slug>[-\w]+)/edit/$', CustomerUpdateView.as_view(), name="customer-update"),
    url(r'^customer/(?P<slug>[-\w]+)/$', CustomerDetailView.as_view(), name='customer-detail'),

    url(r'^products/', ProductListView.as_view(), name='products-list'),
    url(r'^product/create/', ProductCreateView.as_view(), name='product-create'),
    url(r'^product/(?P<slug>[-\w]+)/delete/$', ProductDeleteView.as_view(), name="product-delete"),
    url(r'^product/(?P<slug>[-\w]+)/edit/$', ProductUpdateView.as_view(), name="product-update"),
    url(r'^product/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='product-detail'),



    url(r'^$', IndexView.as_view(), name="index"),



]
