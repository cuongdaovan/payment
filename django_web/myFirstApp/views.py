from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import viewsets
from myFirstApp.serializers import ProductSerializer

from .models import Product, Category, Order, Customer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListProduct(generic.ListView):
    template_name = "myFirstApp/index.html"
    model = Product


class DetailProduct(generic.DetailView):
    template_name = "myFirstApp/detail.html"
    model = Product
    success_url = reverse_lazy('product-list')
    # queryset = Product.objects.all()


class ListCategory(generic.ListView):
    template_name = "myFirstApp/categoryIndex.html"
    queryset = Category.objects.all()


class CategoryDetail(generic.DetailView):
    template_name = "myFirstApp/categoryDetail.html"
    model = Category


class ListOrder(generic.ListView):
    template_name = "myFirstApp/listOrder.html"
    model = Order

    def get_context_data(self, *, object_list=Order, **kwargs):
        data = super().get_context_data()
        data['filter'] = Order.objects.filter(status__startswith="a")
        return data


class DetailOrder(generic.DetailView):
    template_name = "myFirstApp/detailOrder.html"
    model = Order


class UpdateOrder(generic.UpdateView):
    model = Order
    template_name = "myFirstApp/updateOrder.html"
    fields = ['customer', 'payment_type', 'status', 'date']
    template_name_suffix = '_update_form'


class ListCustomer(generic.ListView):
    model = Customer
    template_name = "myFirstApp/listCustomer.html"


class OrderOfCustomer(generic.DetailView):
    model = Customer
    template_name = "myFirstApp/orderOfCustomer.html"
