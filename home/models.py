from django.db import models


class Genre(models.Model):
    """Model for product genres. For example, 'Men', 'Women', 'Children' etc."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Color(models.Model):
    """Model for color saved as HEX codes."""
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """General blueprint for the platform's  products"""
    image = models.ImageField(upload_to='product_images')
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    previous_price = models.DecimalField(max_digits=6, decimal_places=2)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    colors = models.ManyToManyField(Color)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BannerAd(models.Model):
    """Model for top banner ads(They are 3 actually)."""
    image = models.ImageField(upload_to='banner_ads')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
