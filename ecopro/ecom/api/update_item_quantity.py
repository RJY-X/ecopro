from django.http import JsonResponse
from django.shortcuts import redirect
from ecom.api.queries.cart.helpers import update_quantity


def update_item_quantity(request):
    if request.method != "POST":
        redirect("/shop")

    if request.user.is_authenticated is False:
        redirect("/login")

    import json

    data = json.loads(request.body.decode("utf-8"))

    isUpdated = update_quantity(
        id=data["id"], quantity=data["quantity"], cart_total=data["cartTotal"]
    )

    if isUpdated["ok"] is False:
        return JsonResponse({"ok": False, "cause": isUpdated["cause"], "status": 404})

    return JsonResponse(
        {"ok": True, "status": 200, "action": "update", "item": isUpdated["data"]}
    )
