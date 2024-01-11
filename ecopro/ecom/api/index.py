from django.shortcuts import render,redirect
from ecom.api.queries.products.getPopularProducts import get_popular_products

from ecom.forms import ContactForm
from ecom.models import ContactInfo


def index(request):
    products = get_popular_products()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactInfo.objects.create(fullname=form.cleaned_data['fullname'],email=form.cleaned_data['email'],message=form.cleaned_data['message'])
            return redirect('/') 


    return render(request, "ecom/index.html", {**products,"page":"index"})
