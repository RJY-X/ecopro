from ecom.models import Product, ProductImages, ProductVariant, Flavor
from django.shortcuts import get_object_or_404


def get_product_by_id(id: int):
    product = get_object_or_404(Product, id=id)

    # Retrieve related images and variants
    images = ProductImages.objects.filter(product=product)
    variants = ProductVariant.objects.filter(product=product)
    flavors = Flavor.objects.filter(product=product).prefetch_related("flavorimage_set")

    # for element in flavors:
    #     for img in element.flavorimage_set.all():
    #         print(f"flavor: {element.name} --- img: {img.img} --- type: {img.type}")
    first_variant = variants.first()
    first_flavor = flavors.first()
    return {
        "product": {
            "name": product.name,
            "price": first_variant.price,
            "serving": first_variant.serving,
            "description": product.description,
            "flavor_name": first_flavor.name,
            "type": product.type,
            "imgs": images,
            # flavor_imgs
            "flavors": flavors,
            
            
            
        }
    }
