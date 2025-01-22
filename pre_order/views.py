from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import PreOrder
from products.models import Product


def pre_order_confirmation(request, product_id):
    pre_order = get_object_or_404(PreOrder, product_id=product_id, user=request.user)
    quantity = pre_order.quantity
    context = {
        'product': pre_order.product,
        'quantity': quantity,
    }
    return render(request, 'pre_order/confirmation.html', context)


def pre_ordered_products(request):
    pre_orders = PreOrder.objects.filter(user=request.user).select_related('product')
    print("DEBUG: ", pre_orders)

    pre_ordered_product_ids = pre_orders.values_list('product_id', flat=True)

    products = Product.objects.filter(id__in=pre_ordered_product_ids)

    context = {
        'pre_orders': pre_orders,
        'products': products,
        'current_categories': None,
        'current_sorting': 'None_None',
    }

    return render(request, 'pre_order/edit_pre_orders.html', context)

def change_pre_order_quantity(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        print("DEBUG: Quantity entered: ", quantity)

        if quantity and quantity.isdigit() and int(quantity) > 0:
            pre_order = get_object_or_404(PreOrder, product_id=product_id, user=request.user)
            pre_order.quantity = int(quantity)
            pre_order.save()
            print("DEBUG: Quantity recorded in DB: ", pre_order.quantity)

        return redirect(request.META.get('HTTP_REFERER', '/'))


def delete_pre_order(request, product_id):
    if request.method == 'POST':
        pre_order = get_object_or_404(PreOrder, product_id=product_id, user=request.user)
        pre_order.delete()
        messages.success(request, "Your pre-order has successfully been deleted.")
    else:
        messages.error(request, "Invalid request method.")

    return redirect('edit_pre_orders')


def edit_pre_orders(request):
    pre_orders = PreOrder.objects.filter(user=request.user)
    for pre_order in pre_orders:
        print("DEBUG: Pre-order found:", pre_order)

    context = {
        'pre-orders': pre_orders,
    }
    return render(request, 'pre_order/edit_pre_orders.html', context)


def pre_order_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    try:
        pre_order = PreOrder.objects.get(user=request.user, product=product)
        pre_ordered_quantity = pre_order.quantity
        pre_order_date = pre_order.date_preordered

    except PreOrder.DoesNotExist:
        pre_ordered_quantity = 0
        pre_order_date = None

    if request.method =="POST":
        action = request.POST.get("action")
    
        if action == "pre_order":
            if not pre_order:
                PreOrder
    try:
        pre_order = PreOrder.objects.get(user=request.user, product=product)
        pre_ordered_quantity = pre_order.quantity
        pre_order_date = pre_order.date_preordered
    except PreOrder.DoesNotExist:
        pass

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "pre_order":
            PreOrder.objects.create(
                user=request.user,
                product=product,
                quantity=1,
                date_preordered=now(),
            )
            return redirect("pre_order_confirmation")
    
    context = {
        "product": product,
        "pre_ordered_quantity": pre_ordered_quantity,
        "pre_order_date": pre_order_date,
    }
    
    return render(request, "pre_order/pre_order_detail.html", context)
