# Generated by Django 5.0.1 on 2024-01-18 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="product_images")),
                ("product_name", models.CharField(max_length=100)),
                ("colors", models.CharField(max_length=100)),
                ("rating", models.DecimalField(decimal_places=1, max_digits=3)),
                ("featured", models.BooleanField(default=False)),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="home.genre"
                    ),
                ),
            ],
        ),
    ]
