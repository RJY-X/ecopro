from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, null=True)
    product_of_the_week = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Id {self.id}"


class ProductImages(models.Model):
    id = models.AutoField(primary_key=True)
    urls = models.ImageField(upload_to="products/%y/%m/%d")
    type = models.CharField(max_length=50)

    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - Image {self.urls}"


class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serving = models.CharField(max_length=50)

    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - Variant {self.id}"


class FlavorImage(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="flavors/%y/%m/%d")
    type = models.CharField(max_length=50)

    flavor = models.ForeignKey("Flavor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flavor.name} - Image {self.id}"


class Flavor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    product = models.ManyToManyField(Product, through="FlavorToProduct")

    def __str__(self):
        return f"name: {self.name} - id: {self.id}"


class FlavorToProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)

    def __str__(self):
        return f"product id: {self.product} - flavor id: {self.flavor}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_name = models.CharField(max_length=255)
    exp = models.DateField()
    cvv = models.CharField(max_length=4)

    product = models.ManyToManyField(Product, through="OrderToProduct")

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name} - Total: {self.order_total}"


class OrderToProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    flavor = models.CharField(max_length=255)
    serving = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name} - {self.flavor} - {self.serving} - Quantity {self.quantity}"


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart {self.id} - Total: {self.total}"


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flavor = models.CharField(max_length=255)
    serving = models.CharField(max_length=50)

    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"CartItem {self.id} - Product id {self.product.id} - Quantity: {self.quantity} - Price: {self.price} - Serving {self.serving}"


class ContactInfo(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
