from django.urls import path
from rest_framework import routers

from myFirstApp import views




urlpatterns = [
    path('', views.ListProduct.as_view(), name="home"),
    path('<pk>/', views.DetailProduct.as_view(), name="detail"),
    path('category', views.ListCategory.as_view(), name="list_category"),
    path('category/<pk>/', views.CategoryDetail.as_view(), name="category_detail"),
    path('order', views.ListOrder.as_view(), name="order"),
    path('order/<pk>', views.DetailOrder.as_view(), name='detail_order'),
    path('order/update/<pk>', views.UpdateOrder.as_view(), name="update_order"),
    path('customer', views.ListCustomer.as_view(), name="customer"),
    path('customer/<pk>', views.OrderOfCustomer.as_view(), name="order_of_customer"),
    # path('products/', views.ProductViewSet.as_view()),
    # path('categories/', views.CategoryView),
]
