
from rest_framework import serializers
from customer.models import Customer
from Products.models import Products
from Cart.models import Cart


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="___all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="___all__"   

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="___all__"             