# Generated by Django 5.1.7 on 2025-03-25 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_address"),
        ("product", "0003_alter_catagory_parent_catagory_id"),
    ]

    operations = [
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
                ("title", models.CharField(max_length=255)),
                ("details", models.TextField()),
                (
                    "slug_product",
                    models.URLField(max_length=500, null=True, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "catagory_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.catagory",
                    ),
                ),
                (
                    "shop_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.vendor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_varient",
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
                ("title_pv", models.CharField(max_length=255)),
                ("details", models.TextField()),
                ("slug_pv", models.URLField(max_length=500, null=True, unique=True)),
                ("Total_stock", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "catagory_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.catagory",
                    ),
                ),
                (
                    "color_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.color"
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "shop_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.vendor",
                    ),
                ),
                (
                    "size_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.size"
                    ),
                ),
                (
                    "unit_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.unit"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_image",
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
                ("url", models.ImageField(upload_to="images/")),
                ("master_image", models.ImageField(upload_to="images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product_varient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product_varient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product_varient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product_varient",
                    ),
                ),
            ],
        ),
    ]
