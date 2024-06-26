# Generated by Django 4.2.13 on 2024-05-28 07:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100)),
                ('unit', models.CharField(choices=[('Set', 'Set'), ('Piece', 'Piece'), ('Box', 'Box'), ('Unit', 'Unit'), ('Pair', 'Pair')], default='Piece', max_length=10)),
                ('minimum_order_qunatity', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
                ('stock_in_usa', models.BooleanField(default=False)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, null=True, upload_to='images/'), blank=True, null=True, size=8)),
            ],
        ),
    ]
