# Generated by Django 5.0.1 on 2024-11-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_coustomer_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='coustomer',
            name='location',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
