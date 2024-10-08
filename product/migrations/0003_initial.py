# Generated by Django 5.0.1 on 2024-07-11 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_product_category_parent_category'),
        ('origin', '0001_initial'),
        ('product', '0002_delete_product'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo', models.ImageField(upload_to='images/product/prd')),
                ('stock_quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('unit', models.CharField(max_length=10)),
                ('mfg_date', models.DateField()),
                ('sold_quantity', models.IntegerField(default=0, null=True)),
                ('total_review', models.IntegerField(default=0, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.product_category')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='origin.origin')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
        ),
    ]
