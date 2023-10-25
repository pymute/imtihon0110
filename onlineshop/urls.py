from django.urls import path
from . import views
from .views import (UserPurchasesView,TotalInventoryPrice,ExpiredProducts,MostSoldProductView,ProductCreate,CategoryCreate,CustomerCreate,ShoppingCartCreate
)

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/create/', views.CategoryCreate.as_view()),
    path('categories/<pk>/', views.CategoryRetrieve.as_view()),
    path('categories/<pk>/update', views.CategoryUpdate.as_view()),
    path('categories/<pk>/delete', views.CategoryDestroy.as_view()),

    path('products/', views.ProductList.as_view()),
    path('products/create/', views.ProductCreate.as_view()),
    path('products/<pk>/', views.ProductRetrive.as_view()),
    path('products/<pk>/update', views.ProductUpdate.as_view()),
    path('products/<pk>/delete', views.ProductDestroy.as_view()),

    path('customers/', views.CustomerList.as_view()),
    path('customers/create/', views.CustomerCreate.as_view()),
    path('customers/<pk>/', views.CustomerRetrieve.as_view()),
    path('customers/<pk>/update', views.CustomerUpdate.as_view()),
    path('customers/<pk>/delete', views.CustomerDestroy.as_view()),

    path('shopping_carts/', views.ShoppingCartList.as_view()),
    path('shopping_carts/create/', views.ShoppingCartCreate.as_view()),
    path('shopping_carts/<pk>/', views.ShoppingCartRetrieve.as_view()),
    path('shopping_carts/<pk>/update', views.ShoppingCartUpdate.as_view()),
    path('shopping_carts/<pk>/delete', views.ShoppingCartDestroy.as_view()),

    path('items/', views.ItemListView.as_view()),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),

    path('api/customer/<str:user_id>/purchases/', UserPurchasesView.as_view()),

    path('total_inentory_price/', TotalInventoryPrice.as_view(), name='total_inentory_price'),

    path('api/aksiya/<str:customer_id>/', views.PriceCountAPIView.as_view(), name='price_count_api'),

    path('Expired/', ExpiredProducts.as_view(), name='total_inventory_p'),

    path('most-sold-product/', MostSoldProductView.as_view(), name='most-sold-product'),
]
