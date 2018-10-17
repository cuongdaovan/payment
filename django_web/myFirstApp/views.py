from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse,Http404
from django.views import View
from django.views.generic import TemplateView, DetailView,FormView,ListView,UpdateView,DeleteView,RedirectView
from .models import Product,Category,Order, Customer
from django.utils import timezone
from django.urls import reverse_lazy


class ListProduct(ListView):
    template_name = "myFirstApp/index.html"
    model = Product


class DetailProduct(DetailView):
    template_name = "myFirstApp/detail.html"
    model = Product
    success_url = reverse_lazy('product-list')
    # queryset = Product.objects.all()


class ListCategory(ListView):
    template_name = "myFirstApp/categoryIndex.html"
    model = Category


class CategoryDetail(DetailView):
    template_name = "myFirstApp/categoryDetail.html"
    model = Category

class ListOrder(ListView):
    template_name = "myFirstApp/listOrder.html"
    model = Order
    def get_context_data(self, *, object_list=Order, **kwargs):
        data=super().get_context_data()
        data['filter']=Order.objects.filter(status__startswith="a")
        return data
class DetailOrder(DetailView):
    template_name = "myFirstApp/detailOrder.html"
    model = Order

class UpdateOrder(UpdateView):
    model = Order
    template_name = "myFirstApp/updateOrder.html"
    fields = ['customer','payment_type','status','date']
    template_name_suffix = '_update_form'

class ListCustomer(ListView):
    model = Customer
    template_name = "myFirstApp/listCustomer.html"


class OrderOfCustomer(DetailView):
    model = Customer
    template_name = "myFirstApp/orderOfCustomer.html"







