from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product


def index(request):
    products = Product.objects.all()
    return render(request, "main/productlist.html", {"products": products})


def cart(request):
    return render(request, "main/cart.html")


def account(request):
    return render(request, "main/account.html")
