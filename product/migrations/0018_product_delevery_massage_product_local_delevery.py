# Generated by Django 5.0.1 on 2024-08-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delevery_massage',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='local_delevery',
            field=models.BooleanField(default=True, null=True),
        ),
    ]