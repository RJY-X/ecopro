from django.shortcuts import render
from django.http import HttpResponse
from ecom.models import Product



from ecom.forms import LoginForm
from ecom.models import Login

def test(request):
    x = request.POST
    return render(request, "ecom/test.html", {"pro":Product.objects.all()})



def fr(request):
        return render(request, 'ecom/test.html')