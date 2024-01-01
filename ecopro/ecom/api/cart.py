from django.shortcuts import render

def cart(request):
    return render(request, "ecom/cart.html") 