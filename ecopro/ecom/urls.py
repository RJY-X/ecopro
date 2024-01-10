from django.urls import path

from . import views


app_name = "ecom"

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.Alogin, name="login"),
    path("signup",views.signup,name="signup"),
    path("shop",views.shop, name="shop"),
    path("cart",views.cart, name="cart"),
    path("products",views.products, name="products"),
    path("test",views.fr, name="test"),
    path("profile",views.profile,name="profile"),


]