from django.shortcuts import render

def products(request):
    return render(request, "ecom/products.html") 