from django.shortcuts import render, redirect
from ecom.forms import SignupForm
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

# def signup(request):
#     if request.method=='POST':
#         username = request.POST.get('first-name')
#         password = request.POST.get('password')
#         firstname = request.POST.get('first-name')
#         lastname = request.POST.get('last-name')
#         email = request.POST.get('email')
#         form_data = {
#             'username': username,
#             'password': password,
#             'first_name': firstname,
#             'last_name': lastname,
#             'email': email,
#         }
#         form = SignupForm(data=form_data)
#         if form.is_valid():
#             form.save()
#             return render(request, 'ecom/sign_up.html', {'message': "Signed up successfully"})
#         else:
#             return render(request, 'ecom/sign_up.html', {'message': "Form is not valid. Please check your inputs."})

#     else:
#         return render(request, 'ecom/sign_up.html', {'message':"not sign in"})

def signup(request):
    if request.method == "POST":
        userData = request.POST.copy()
        userData["password1"] = request.POST.get("password")
        userData["password2"] = request.POST.get("password")
        userData["username"] = get_random_string(length=50)

        form = SignupForm(userData)

        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                return render(
                    request,
                    "ecom/sign_up.html",
                    {
                        "error_global": "this email is already being used by a different account, try to sign up with a different one",
                    },
                )
            # insert user into database
            form.save()
            return redirect("/")
        else:
            errors = {}

            # for field, err in form.errors.items():
            #     print(f"Field: {field}, Errors: {', '.join(errors)}")
            #     errors[field] = err
            for field, err in form.errors.items():
                print(f"Field: {field}, Errors: {', '.join(err)}")
                print(', '.join(err))
                errors[field] = ', '.join(err)

            return render(request, "ecom/sign_up.html", {"errors": errors})

    else:
        return render(request, "ecom/sign_up.html")
        