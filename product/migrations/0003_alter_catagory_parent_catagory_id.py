# Generated by Django 5.1.7 on 2025-03-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_catagory_color_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catagory",
            name="parent_catagory_id",
            field=models.IntegerField(),
        ),
    ]
