from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="main"),
    path("cart/", views.cart, name="cart"),
    path("account/", views.account, name="account"),
]
