from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib import admin

app_name = "ecom"

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("login", views.Alogin, name="login"),
    path("signup", views.signup, name="signup"),
    path("shop", views.shop, name="shop"),
    path("cart", views.cart, name="cart"),
    path("cart/add_to_cart", views.add_to_cart, name="add_cart_item"),
    path(
        "cart/update_item_quantity",
        views.update_item_quantity,
        name="update_item_quantity",
    ),
    path(
        "cart/add_order",
        views.add_order_handler,
        name="add_order",
    ),
    path(
        "cart/delete_cart_item", views.delete_cart_item_handler, name="delete_cart_item"
    ),
    path("products", views.redirect_to_shop, name="redirect_to_shop"),
    path("products/<int:id>", views.products, name="product"),
    path("signout", views.sign_out_handler, name="signout"),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
