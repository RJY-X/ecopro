from django.shortcuts import render,redirect
from ecom.models import Order

def cart(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        cart_name = request.POST['cart_name']
        exp = request.POST['exp']
        cvv = request.POST['cvv']

        # Créer une instance du modèle avec les données du formulaire
        paiement = Order(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            cart_name=cart_name,
            exp=exp,
            cvv=cvv,
        )
        print(f"Email: {email}, first_name: {first_name}, last_name:{last_name}")        

        # Rediriger vers une page de confirmation ou une autre page
        return redirect('/cart')

    # Si la méthode de requête n'est pas POST, afficher simplement le formulaire
    return render(request, 'ecom/cart.html')




    