from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200,default='Aziz')
    location = models.CharField(max_length=100, blank=True, null=True)
    address = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True)
    
    def total(self):
        items = self.items.all()
        total = sum([item.product.price * item.quantity for item in items])
        return total
    def __str__(self):
        return self.customer.name 

class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop_cart = models.ForeignKey(ShoppingCart, related_name='items', on_delete=models.CASCADE)
    sell_date = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
