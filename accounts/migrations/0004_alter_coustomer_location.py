# Generated by Django 5.0.1 on 2024-11-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_coustomer_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomer',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
