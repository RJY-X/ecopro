from django.contrib import admin
from .models import ContactInfo
from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderToProduct,
    ProductVariant,
    ProductImages,
    Flavor,
    FlavorImage,
    FlavorToProduct,
)

# Register your models here.
admin.site.register(Product)

admin.site.site_header='APOSTEl PANEL'
admin.site.site_title='APOSTEl PANEL'

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderToProduct)
admin.site.register(ProductVariant)
admin.site.register(ProductImages)
admin.site.register(Flavor)
admin.site.register(FlavorToProduct)
admin.site.register(FlavorImage)


admin.site.register(ContactInfo)



