# Generated by Django 5.0.1 on 2024-08-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_update_at_alter_product_sold_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
