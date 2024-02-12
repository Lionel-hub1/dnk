from django.contrib import admin

from .models import Genre, Product, Color, BannerAd

admin.site.register(Genre)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(BannerAd)

# Other Django Admin Modifications
admin.site.site_header = "DNK Store Admin Panel"
