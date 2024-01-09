from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#    
#     active = models.BooleanField(default = True)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    urls = models.ImageField(upload_to='static/products/%y/%m/%d')

class ProductToImage(models.Model):
    id = models.AutoField(primary_key=True)
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_id.name} - Image {self.image_id.id}"

class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serving = models.CharField(max_length=50)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - Variant {self.id}"
    
class FlavorImage(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='static/products/flavors/%y/%m/%d')  # Assuming images are uploaded to a 'flavor_images/' directory, adjust accordingly
    flavor = models.ForeignKey('Flavor', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.flavor.name} - Image {self.id}"    

class Flavor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OrderToProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    flavor = models.CharField(max_length=255)
    serving = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name} - {self.flavor} - {self.serving} - Quantity {self.quantity}"
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_name = models.CharField(max_length=255)
    exp = models.DateField()  
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name} - Total: {self.order_total}"

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart {self.id} - Total: {self.total}"
    
class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cart_id = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"CartItem {self.id} - Quantity: {self.quantity} - Total: {self.total}"