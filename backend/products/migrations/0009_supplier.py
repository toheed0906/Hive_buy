# Generated by Django 4.2.13 on 2024-05-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50, verbose_name='name')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('certifications', models.ManyToManyField(blank=True, to='products.suppliercertification')),
            ],
        ),
    ]