# Generated by Django 5.0.1 on 2024-01-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_color_color"),
    ]

    operations = [
        migrations.CreateModel(
            name="BannerAd",
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
                ("image", models.ImageField(upload_to="banner_ads")),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]
