from django.http import JsonResponse
from django.shortcuts import redirect
from ecom.api.queries.cart.helpers import (
    check_for_item,
    create_cart_item,
    check_for_cart,
    create_cart,
)


def add_to_cart(request):
    if request.method != "POST":
        redirect("/shop")

    if request.user.is_authenticated is False:
        return JsonResponse(
            {"ok": False, "cause": "missing user is not authenticated", "status": 401}
        )

    import json

    data = json.loads(request.body.decode("utf-8"))
    user_id = request.user.id

    # print(f"user_id ---- {user_id} ---- data.price --- {data['price']}")

    # check if user has a cart
    maybe_cart = check_for_cart(user_id)

    if maybe_cart["ok"] is False:
        total = 0
        maybe_cart["data"] = create_cart(user_id, total)

    maybe_item = check_for_item(product_id=data["productId"])

    return JsonResponse(
        {"ok": True, "maybe_item": maybe_item, "maybe_cart": maybe_cart}
    )

    # check if it is the same product with the same
    # flavor and serving size if so increase
    # the quantity else add the item
    # into the cart
    # if maybe_item.ok:
    #     item = maybe_item.data
    #     if item.flavor == data.flavor and item.serving == data.serving:
    #         if item.quantity == data.quantity:
    #             return JsonResponse({"ok": True, "status": 200, "action": "nothing"})

    # increase qty
    # item.quantity = item.quantity + 1
    # return JsonResponse({"ok": True, "status": 200, "action": "update item"})

    # else:
    #     maybe_new_item = create_cart_item(cart=maybe_cart.data, data=data)

    # if maybe_new_item.ok is False:
    #     return JsonResponse(
    #         {"ok": False, "cause": maybe_new_item.cause, "status": 500}
    #     )

    # new_item = maybe_new_item.data
    # increase cart total
    # cart = maybe_cart.data
    # cart.total = cart.total + new_item.price
    # cart.save()

    # return JsonResponse(
    #     {
    #         "ok": True,
    #         "status": 200,
    #         "action": "create",
    #         "item": new_item,
    #     }
    # )
