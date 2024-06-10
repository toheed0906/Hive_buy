# Generated by Django 4.2.13 on 2024-05-28 09:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(max_length=20, upload_to='images/'), blank=True, default=list, size=2),
        ),
    ]