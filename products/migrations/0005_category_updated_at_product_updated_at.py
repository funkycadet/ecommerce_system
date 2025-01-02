# Generated by Django 5.1.4 on 2025-01-02 18:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_category_options_alter_discount_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]