from django.shortcuts import render


def products(request, id):
    print(f"id - {id}")
    return render(request, "ecom/products.html")
