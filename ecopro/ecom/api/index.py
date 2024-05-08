from django.shortcuts import render, redirect
from ecom.api.queries.products.getPopularProducts import get_popular_products
from ecom.api.queries.products.getProductOfTheWeek import get_product_of_the_week

from ecom.forms import ContactForm
from ecom.models import ContactInfo


def index(request):
    products = get_popular_products()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactInfo.objects.create(
                fullname=form.cleaned_data["fullname"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
            )
            return redirect("/")

    product_of_the_week = get_product_of_the_week()

    return render(
        request,
        "ecom/index.html",
        {**products, "page": "index", "product_of_the_week": product_of_the_week},
    )
