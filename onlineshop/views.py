from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import models
from django.utils import timezone
from django.views import View
from django.db.models import Sum,F
from rest_framework.views import APIView
from config.permissions import AdminPermission, AuthorPermission
from django.db.models import Sum
from rest_framework import views,response,status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Category, Product, Customer, ShoppingCart,Items
from .serializers import CategorySerializer,ItemsSerializer, ProductSerializer, CustomerSerializer, ShoppingCartSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShoppingCartList(generics.ListAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartCreate(generics.CreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class CategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroy(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrive(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerRetrieve(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDestroy(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShoppingCartUpdate(generics.UpdateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartDestroy(generics.DestroyAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartRetrieve(generics.RetrieveAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    
class ItemDetailView(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemCreateView(generics.CreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemUpdateView(generics.UpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemListView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemDeleteView(generics.DestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class UserPurchasesView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
       user_id = self.kwargs['user_id']
       return Items.objects.filter(shop_cart__customer=user_id)
    
class TotalInventoryPrice(APIView):
    queryset = Product.objects.all()
    
    def get(self, request):
        total_price = Product.objects.aggregate(total=Sum('price'))  # Assumes each Product has a 'price' field
        return Response({"total_price": total_price['total']})
    
class ExpiredProducts(generics.ListAPIView):   
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(end_date__lt=timezone.now())
    

class MostSoldProductView(APIView):
    
    def get(self, request, format=None):
        grouped_sales = Items.objects.values('product__name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')
        
        most_sold_product_info = grouped_sales.first()

        if most_sold_product_info:
            most_sold_product_id = most_sold_product_info['product__name']
            
            data = {'kop sotilgan mahsulot': most_sold_product_id}
            
            return Response(data)
        else:
            return Response({'error': 'No items have been sold yet.'})

    
class PriceCountAPIView(APIView):
    queryset = ShoppingCart.objects.all()

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        shopping_carts = ShoppingCart.objects.filter(customer_id=customer_id)
        expensive_products = Product.objects.filter(Q(id__in=[item.product_id for cart in shopping_carts for item in cart.items.all()]) & Q(price__gt=100))
        total_price = sum(product.price for product in expensive_products)
        total_million = 'Mijozning umumiy haridi 1000000 so\'mdan oshgan' if total_price > 1000000 else 'Mijozning umumiy haridi 1000000 so\'mdan oshmagan'
            
        return Response({"customer_name": customer.name, "count": expensive_products.count(), "total_price": total_price, 'Natija': total_million})
