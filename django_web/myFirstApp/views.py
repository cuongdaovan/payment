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
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['list_product']= Product.objects.all()
        return context

class DetailProduct(DetailView):
    template_name = "myFirstApp/detail.html"
    model = Product
    success_url = reverse_lazy('product-list')
    # queryset = Product.objects.all()
    def get_context_data(self,*,object=None, **kwargs):
        context= super(DetailProduct,self).get_context_data(**kwargs)
        context['list_product']=Product.objects.all()
        return context

class ListCategory(ListView):
    template_name = "myFirstApp/categoryIndex.html"
    model = Category
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(ListCategory, self).get_context_data(**kwargs)
        context['list_category']=Category.objects.all()
        return context

class CategoryDetail(DetailView):
    template_name = "myFirstApp/categoryDetail.html"
    model = Category

class ListOrder(ListView):
    template_name = "myFirstApp/listOrder.html"
    model = Order
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context["order_list"]=Order.objects.all()
        return context

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
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context["customer_list"]=Customer.objects.all()
        return context

class OrderOfCustomer(DetailView):
    model = Customer
    template_name = "myFirstApp/orderOfCustomer.html"










