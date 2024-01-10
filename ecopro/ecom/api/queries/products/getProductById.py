from ecom.models import Product


def get_product_by_id(id: int):
    product = Product.objects.filter(id=id).prefetch_related(
        "productvariant_set", "productimages_set"
    )

    # productFromFlavor = Product.filter(flavor__)
