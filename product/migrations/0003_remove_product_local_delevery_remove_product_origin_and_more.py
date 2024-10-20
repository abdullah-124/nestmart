# Generated by Django 5.0.1 on 2024-10-20 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('origin', '0003_location'),
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='local_delevery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='origin.location'),
        ),
        migrations.AddField(
            model_name='product',
            name='review_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
