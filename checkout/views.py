from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PfcafGoyyD5nsFCFUrsLfRkp6iSwkQURmJUAln3oVAGceCoy43AxNed4tDhymBW1PcrpLZRb70gEFKE5aJFWCeN00eyIQZXzL',
        'client_secret': 'test client secret code',
    }

    return render(request, template, context)