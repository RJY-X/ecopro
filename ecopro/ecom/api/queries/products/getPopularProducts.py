from ecom.models import Product


def get_popular_products():
    limit = 10
    data = Product.objects.prefetch_related("productvariant_set").prefetch_related(
        "productimages_set"
    )[:limit]

    products = []
    for p in data:
        url = None

        for img in p.productimages_set.all():
            if img.type == "main":
                url = img.urls

        variant = p.productvariant_set.first()
        products.append(
            {"name": p.name, "url": url, "price": variant.price, "id": p.id}
        )

    return {"products": products}
