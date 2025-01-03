# Generated by Django 5.0.1 on 2024-11-04 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=30)),
                ('image', models.ImageField(upload_to='images/category/')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.product_category')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(null=True, upload_to='images/category/sub_cat/')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.product_category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
