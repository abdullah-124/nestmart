# Generated by Django 5.0.1 on 2024-10-20 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('origin', '0003_location'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='rating',
        ),
        migrations.AddField(
            model_name='seller',
            name='Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='origin.location'),
        ),
        migrations.AddField(
            model_name='seller',
            name='review_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='total_review',
            field=models.IntegerField(default=0, null=0),
        ),
    ]
