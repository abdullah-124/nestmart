# Generated by Django 5.0.1 on 2024-07-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_brand_alter_product_exp_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
    ]
