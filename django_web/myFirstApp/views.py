# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    login as auth_login,
)

from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt import tokens
from rest_framework_simplejwt import serializers as jwt_serializer

from myFirstApp import serializers
from myFirstApp import models


class Login(views.LoginView):
    token = None

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        self.token = jwt_serializer.TokenObtainPairSerializer.get_token(user=self.request.user)
        print(self.token)
        # self.token = tokens.AccessToken().for_user(user=self.request.user)
        response = HttpResponseRedirect(self.get_success_url())
        response.set_cookie('token', self.token)
        return response


class CategoryViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        data = {'token': request.COOKIES.get('token')}
        valid_data = jwt_serializer.TokenVerifySerializer().validate(data)
        queryset = models.Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        data = {'token': request.COOKIES.get('token')}
        valid_data = jwt_serializer.TokenVerifySerializer().validate(data)
        if valid_data == '':
            queryset = models.Category.objects.all()
            print('cuong')
        else:
            queryset = None
        serializer = serializers.CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {'refresh': request.COOKIES.get('token')}
        token = None
        token = jwt_serializer.TokenRefreshSerializer.validate(self, data)
        print(token)
        queryset = models.Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)
        response = Response({'product-list': serializer.data, 'token': str(token)})
        # response.set_cookie('token', token)
        return response


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