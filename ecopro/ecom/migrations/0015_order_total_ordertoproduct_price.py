# Generated by Django 5.0 on 2024-01-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0014_product_product_of_the_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='ordertoproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
