# Generated by Django 5.0.1 on 2024-08-11 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_seller_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='total_product',
        ),
    ]