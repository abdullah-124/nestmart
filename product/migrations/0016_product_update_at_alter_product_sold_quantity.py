# Generated by Django 5.0.1 on 2024-08-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_mfg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_quantity',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]