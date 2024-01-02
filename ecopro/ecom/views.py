from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, "ecom/index.html", {"name":"Amjad khawi"})

def login(request):
    return render(request, "ecom/login page.html") 

def signin(request):
    return render(request, "ecom/sign_in.html")