from django.shortcuts import render
from ecom.api.queries.products.getPopularProducts import get_popular_products


def index(request):
    products = get_popular_products()

    return render(request, "ecom/index.html", {**products})
