from django.shortcuts import render
from ecom.api.queries.products.getProductById import get_product_by_id
from ecom.api.queries.products.getPopularProducts import get_popular_products


def products(request, id):
    product = get_product_by_id(id)
    similar_products = get_popular_products()
    return render(
        request, "ecom/products.html", {**product, "similar_products": similar_products}
    )
