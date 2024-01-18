from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='product_images')
    product_name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    colors = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
