from rest_framework import serializers

from myFirstApp import models


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = models.Product
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = models.Category
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('__all__')


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'products')