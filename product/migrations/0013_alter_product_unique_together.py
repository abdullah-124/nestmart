# Generated by Django 5.0.1 on 2024-07-23 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_product_category_name'),
        ('product', '0012_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('category',)},
        ),
    ]
