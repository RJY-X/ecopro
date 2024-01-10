from django.shortcuts import render
from ecom.api.queries.products.getProductById import get_product_by_id


def products(request, id):
    print(f"id - {id}")
    product=get_product_by_id(id)
    return render(request, "ecom/products.html",{**product})
