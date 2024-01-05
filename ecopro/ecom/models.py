from django.db import models



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='static/products/%y/%m/%d')
    active = models.BooleanField(default = True)


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



