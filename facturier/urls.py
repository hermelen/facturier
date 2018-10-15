from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


from app.views import IndexView, CustomerCreateView, CustomerDetailView, CustomerUpdateView, CustomerDeleteView, CustomerListView
from app.views import ProductCreateView, ProductDetailView, ProductUpdateView,ProductListView, ProductDeleteView
from app.views import QuotationDetailView, QuotationCreateView, QuotationListView, QuotationPdfDetailView
from app.views import ProductListUpdateView, ProductListDeleteView, ProductListCreateView
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

    url(r'^quotations/', QuotationListView.as_view(), name='quotations-list'),
    url(r'^quotation/create/', QuotationCreateView.as_view(), name='quotation-create'),
    url(r'^quotation/pdf/(?P<slug>[-\w]+)/$', QuotationPdfDetailView.as_view(), name='quotation-pdf'),
    url(r'^quotation/(?P<slug>[-\w]+)/$', QuotationDetailView.as_view(), name='quotation-detail'),

    url(r'^productlist/(?P<id>[-\w]+)/delete$', ProductListDeleteView.as_view(), name="productlist-delete"),
    url(r'^productlist/(?P<id>[-\w]+)/(?P<field>[-\w]+)/edit$', ProductListUpdateView.as_view(), name="productlist-update"),
    url(r'^productlist/(?P<id>[-\w]+)/add$', ProductListCreateView.as_view(), name="productlist-create"),

    url(r'^$', IndexView.as_view(), name='index'),




]
