# Generated by Django 5.0.1 on 2024-07-15 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_sub_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.product_category'),
        ),
    ]
