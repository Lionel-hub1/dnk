"""Module for views of the dnk app."""
from django.shortcuts import render
from .models import Product


def index(request):
    selectedProducts = Product.objects.all()
    print(selectedProducts[1].colors.all())
    return render(request, "index.html", {"products": selectedProducts})
