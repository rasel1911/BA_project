# Generated by Django 5.1.7 on 2025-03-24 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("shop_name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=255)),
                ("slug", models.URLField(max_length=500, null=True, unique=True)),
                ("image", models.ImageField(upload_to="images/")),
                ("description", models.TextField()),
                ("tradelicense", models.CharField(max_length=255, unique=True)),
                ("rating", models.IntegerField()),
                ("status", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "seller_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
                    ),
                ),
            ],
        ),
    ]
