from django.urls import path

from . import views
from django.views.generic import TemplateView
from myFirstApp.views import ListProduct,DetailProduct,ListCategory,\
    CategoryDetail,ListOrder,DetailOrder,UpdateOrder,ListCustomer,OrderOfCustomer

urlpatterns = [
    path('',ListProduct.as_view(),name="home"),
    path(r'<pk>/',DetailProduct.as_view(),name="detail"),
    path(r'category',ListCategory.as_view(),name="list_category"),
    path(r'category/<pk>/',CategoryDetail.as_view(),name="category_detail"),
    path(r'order',ListOrder.as_view(),name="order"),
    path(r'order/<pk>',DetailOrder.as_view(),name='detailOrder'),
    path(r'order/update/<pk>',UpdateOrder.as_view(),name="updateOrder"),
    path(r'customer',ListCustomer.as_view(),name="customer"),
    path(r'customer/<pk>',OrderOfCustomer.as_view(),name="orderOfCustomer")
]