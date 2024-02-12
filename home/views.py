"""Module for views of the dnk app."""
from django.shortcuts import render
from .models import Product, BannerAd


def index(request):
    selectedProducts = Product.objects.all()
    selectedBannerAds = BannerAd.objects.all()
    return render(request, "index.html", {"products": selectedProducts, "banner_ads": selectedBannerAds})
