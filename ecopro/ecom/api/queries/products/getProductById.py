from ecom.models import Product, ProductImages, ProductVariant, Flavor
from django.shortcuts import get_object_or_404


def get_product_by_id(id: int):
    product = get_object_or_404(Product, id=id)

    # Retrieve related images and variants
    images = ProductImages.objects.filter(product=product)
    variants = ProductVariant.objects.filter(product=product)
    flavors = Flavor.objects.filter(product=product).prefetch_related("flavorimage_set")

    flavors_data = []

    for flavor in flavors:
        flavors_data.append(
            {
                "name": flavor.name,
                "large_img": flavor.flavorimage_set.filter(type="large").first().img,
                "medium_img": flavor.flavorimage_set.filter(type="medium").first().img,
                "small_img": flavor.flavorimage_set.filter(type="small").first().img,
            }
        )

    first_variant = variants.first()
    first_flavor = flavors.first()

    first_flavor_imgs = {}
    for img in first_flavor.flavorimage_set.all():
        if img.type == "small":
            first_flavor_imgs.update({"small_img": img.img})
        if img.type == "medium":
            first_flavor_imgs.update({"medium_img": img.img})
        if img.type == "large":
            first_flavor_imgs.update({"large_img": img.img})

    return {
        "product": {
            "name": product.name,
            "price": first_variant.price,
            "serving": first_variant.serving,
            "description": product.description,
            "first_flavor": {**first_flavor_imgs, "name": first_flavor.name},
            "type": product.type,
            "id": product.id,
            "imgs": images,
            "varients": variants,
            "flavors": flavors_data,
        }
    }
