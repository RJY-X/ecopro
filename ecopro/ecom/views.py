
from django.shortcuts import render
from django.http import HttpResponse
from ecom.api.index import index
from ecom.api.shop import shop
from ecom.api.login import login
from ecom.api.cart import cart
from ecom.api.products import products

def signin(request):
    return render(request, "ecom/login page.html")





