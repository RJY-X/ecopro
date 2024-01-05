from django.shortcuts import render
from ecom.forms import SignupForm

def signup(request):
    if request.method=='POST':
        username = request.POST.get('first-name')
        password = request.POST.get('password')
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        email = request.POST.get('email')
        data = SignupForm(request, username=username, password=password, firstname=firstname, lastname=lastname, email=email)
        data.save()
        return render(request, 'ecom/sign_up.html', {'message':"is sign in"})

    else:
        return render(request, 'ecom/sign_up.html', {'message':"not sign in"})