from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path("", views.product_list, name="main"),
    path("cart/", views.cart, name="cart"),
    path("account/", views.account, name="account"),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
