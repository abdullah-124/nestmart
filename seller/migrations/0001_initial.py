# Generated by Django 5.0.1 on 2024-10-20 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('origin', '0002_origin_district'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50, unique=True)),
                ('photo', models.ImageField(upload_to='images/seller/')),
                ('mobile', models.CharField(max_length=12)),
                ('product_sell', models.IntegerField(default=0, null=True)),
                ('sell_amount', models.IntegerField(default=0, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, null=True)),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='origin.origin')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
