# Generated by Django 5.1.7 on 2025-03-29 17:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_rename_type_user_data_type_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_data",
            name="email",
        ),
        migrations.RemoveField(
            model_name="user_data",
            name="name",
        ),
        migrations.RemoveField(
            model_name="user_data",
            name="password",
        ),
        migrations.AddField(
            model_name="user_data",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
