from django.contrib import admin
from .models import ShoppingCart,Category,Customer,Product,Items
# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Items)
