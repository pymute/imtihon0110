from rest_framework import serializers
from .models import Category, Product, Customer, ShoppingCart,Items

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','id']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id','name', 'price','category','start_date','end_date']

class CustomerSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Customer
        fields = ['id','location','name','phone','address']

class ShoppingCartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = ShoppingCart
        fields = ['id','customer','payment','date']

class ItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Items
        fields = ['id','product','sell_date','shop_cart','quantity']
