"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import routers, urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from myFirstApp import views

router = routers.SimpleRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('categories', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('myFirstApp.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/refresh-token/', TokenRefreshView.as_view()),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
# urls.urlpatterns = [
#     path('login/', views.Login.as_view(template_name='rest_framework/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
