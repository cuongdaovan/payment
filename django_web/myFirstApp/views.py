from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from myFirstApp import serializers
from myFirstApp import models


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ListCategoryAPI(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(generics.ListCreateAPIView):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ListOrderAPI(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ListProduct(generic.ListView):
    template_name = 'myFirstApp/index.html'
    model = models.Product


class DetailProduct(generic.DetailView):
    template_name = 'myFirstApp/detail.html'
    model = models.Product
    success_url = reverse_lazy('product-list')
    # queryset = Product.objects.all()


class ListCategory(generic.ListView):
    template_name = 'myFirstApp/categoryIndex.html'
    queryset = models.Category.objects.all()


class CategoryDetail(generic.DetailView):
    template_name = 'myFirstApp/categoryDetail.html'
    model = models.Category


class ListOrder(generic.ListView):
    template_name = 'myFirstApp/listOrder.html'
    model = models.Order

    def get_context_data(self, *, object_list=models.Order, **kwargs):
        data = super().get_context_data()
        data['filter'] = models.Order.objects.filter(status__startswith='a')
        return data


class DetailOrder(generic.DetailView):
    template_name = 'myFirstApp/detailOrder.html'
    model = models.Order


class UpdateOrder(generic.UpdateView):
    model = models.Order
    template_name = 'myFirstApp/updateOrder.html'
    fields = ['customer', 'payment_type', 'status', 'date']
    template_name_suffix = '_update_form'


class ListCustomer(generic.ListView):
    model = models.Customer
    template_name = 'myFirstApp/listCustomer.html'


class OrderOfCustomer(generic.DetailView):
    model = models.Customer
    template_name = 'myFirstApp/orderOfCustomer.html'
