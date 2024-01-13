from django.contrib.auth import logout
from django.shortcuts import redirect


def sign_out_handler(request):
    logout(request)
    return redirect("/")
