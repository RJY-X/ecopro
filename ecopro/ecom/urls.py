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
    path("cart/add_to_cart", views.add_to_cart, name="add cart item"),
    path("products", views.redirect_to_shop, name="redirect to shop"),
    path("products/<int:id>", views.products, name="product"),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
