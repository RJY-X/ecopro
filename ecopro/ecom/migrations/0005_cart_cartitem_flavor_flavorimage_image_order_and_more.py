# Generated by Django 5.0 on 2024-01-09 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_login'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FlavorImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='static/products/flavors/%y/%m/%d')),
                ('type', models.CharField(max_length=50)),
                ('flavor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.flavor')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('urls', models.ImageField(upload_to='static/products/%y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart_name', models.CharField(max_length=255)),
                ('exp', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderToProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('flavor', models.CharField(max_length=255)),
                ('serving', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductToImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.image')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serving', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product'),
        ),
        migrations.AddField(
            model_name='ordertoproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product'),
        ),
        migrations.AddField(
            model_name='producttoimage',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product'),
        ),
    ]
