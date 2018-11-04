from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.response import Response

from myFirstApp import serializers
from myFirstApp import models


class CategoryViewSet(viewsets.ViewSet):
    """docstring for CategoryViewSet"""
    def list(self, request):
        queryset = models.Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)
        return Response(serializer.data)
        

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = models.Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ListProduct(generic.ListView):
    template_name = "myFirstApp/index.html"
    model = models.Product


class DetailProduct(generic.DetailView):
    template_name = "myFirstApp/detail.html"
    model = models.Product
    success_url = reverse_lazy('product-list')
    # queryset = Product.objects.all()


class ListCategory(generic.ListView):
    template_name = "myFirstApp/categoryIndex.html"
    queryset = models.Category.objects.all()


class CategoryDetail(generic.DetailView):
    template_name = "myFirstApp/categoryDetail.html"
    model = models.Category


class ListOrder(generic.ListView):
    template_name = "myFirstApp/listOrder.html"
    model = models.Order

    def get_context_data(self, *, object_list=models.Order, **kwargs):
        data = super().get_context_data()
        data['filter'] = models.Order.objects.filter(status__startswith="a")
        return data


class DetailOrder(generic.DetailView):
    template_name = "myFirstApp/detailOrder.html"
    model = models.Order


class UpdateOrder(generic.UpdateView):
    model = models.Order
    template_name = "myFirstApp/updateOrder.html"
    fields = ['customer', 'payment_type', 'status', 'date']
    template_name_suffix = '_update_form'


class ListCustomer(generic.ListView):
    model = models.Customer
    template_name = "myFirstApp/listCustomer.html"


class OrderOfCustomer(generic.DetailView):
    model = models.Customer
    template_name = "myFirstApp/orderOfCustomer.html"
