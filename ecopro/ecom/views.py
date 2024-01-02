
def signin(request):
    return render(request, "ecom/sign_in.html")

from ecom.api.index import index
from ecom.api.shop import shop
from ecom.api.login import login
from ecom.api.cart import cart

