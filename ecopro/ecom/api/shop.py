from django.shortcuts import render
from ecom.api.queries.products.getAllProducts import get_all_products
from ecom.api.queries.products.getProductsByType import get_products_by_type


def shop(request):
    products = {}

    filter = request.GET.get("filter", "")

    if filter == "protein" or filter == "pre-workout" or filter == "creatine":
        products = get_products_by_type(filter)
    else:
        products = get_all_products()

    return render(request, "ecom/shop.html", {**products, "filter": filter})
