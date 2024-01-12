from django.contrib.auth.models import User
from ecom.models import CartItem
from ecom.models import Cart, Product


def check_for_cart(user_id):
    try:
        cart = Cart.objects.get(user__id=user_id)
        return {"ok": True, "data": cart}

    except Cart.DoesNotExist:
        return {"ok": False, "data": None}


def check_for_item(cart, product_id, serving, flavor):
    try:
        item = CartItem.objects.get(
            cart_id=cart, product__id=product_id, serving=serving, flavor=flavor
        )

        return {"ok": True, "data": item}

    except CartItem.DoesNotExist:
        return {"ok": False, "data": None}


def create_cart(user_id, total):
    user = User.objects.get(id=user_id)
    cart = Cart.objects.create(total=total, user=user)

    return cart


def create_cart_item(cart, data):
    try:
        product = Product.objects.get(id=data["productId"])
        item = CartItem.objects.create(
            quantity=data["quantity"],
            price=data["price"],
            flavor=data["flavor"],
            serving=data["serving"],
            cart_id=cart,
            product=product,
        )
        return {"ok": True, "data": item}

    except Product.DoesNotExist:
        return {"ok": False, "cause": "product"}
