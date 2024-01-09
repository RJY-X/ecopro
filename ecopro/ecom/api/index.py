from django.shortcuts import render
from django.http import HttpResponse
from ecom.models import Product,ProductToImage

def index(request):
    products=Product.objects.all()
    product_images = {}
    for product in products:
        images = ProductToImage.objects.filter(product_id=product.id)
        product_images[product] = images
    print(product_images)
    return render(request, "ecom/index.html", {"products":products,'product_images': product_images})


