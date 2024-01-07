from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from ecom.forms import LoginForm 
from django.contrib.auth.models import User


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             print(f"Email: {email}, Password: {password}")
#             user = authenticate(request, email=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('ecom/index.html')  # Replace 'home' with the name of your home URL
#             else:
#                 error_message = 'Invalid login credentials. Please try again.'
#                 return render(request, 'ecom/login page.html', {'form': form, 'error_message': error_message})
#     else:
#         form = LoginForm()

#     return render(request, 'ecom/login page.html', {'form': form})



def Alogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email)
                if username is not None:
                    user = authenticate(request, username=username, password=password)
                    print(f"Email: {email}, Password: {password}, user:{user}")

                    if user is not None:
                       login(request, user)
                       return redirect('/')
            except User.DoesNotExist:
                return render(request, 'ecom/login page.html', {'error_message': "this user does not exist"})
            
        error_message = 'Invalid login credentials. Please try again.'
        return render(request, 'ecom/login page.html', {'error_message': error_message})
        
  
    else:
        return render(request, 'ecom/login page.html')