from django.shortcuts import render


def pre_order_confirmation(request):
    return render(request, 'pre_order/confirmation.html')