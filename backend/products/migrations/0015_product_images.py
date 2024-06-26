# Generated by Django 4.2.13 on 2024-05-28 09:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=[], size=2),
        ),
    ]
