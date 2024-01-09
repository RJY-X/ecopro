from django.contrib import admin
from .models import Product,Cart,CartItem,Order,OrderToProduct,ProductVariant,ProductToImage,Image,Flavor,FlavorImage

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderToProduct)
admin.site.register(ProductVariant)
admin.site.register(ProductToImage)
admin.site.register(Image)
admin.site.register(Flavor)
admin.site.register(FlavorImage)


