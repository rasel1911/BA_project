# Generated by Django 5.1.7 on 2025-04-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_product_product_varient_product_image_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product_varient",
            name="slug_pv",
            field=models.URLField(max_length=500, null=True),
        ),
    ]
