# Generated by Django 5.1.7 on 2025-03-28 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_user_data_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_data",
            old_name="type",
            new_name="type_user",
        ),
    ]
