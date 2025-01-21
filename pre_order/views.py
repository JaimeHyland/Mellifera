from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import PreOrder
from products.models import Product


def pre_order_confirmation(request):
    return render(request, 'pre_order/confirmation.html')


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

        if action == add_to_bag:
            pass

    
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

        if action == "add_to_bag":
            bag = request.session.get("bag", {})
            bag[str(product.id)] = bag.get(str(product.id), 0) + 1
            request.session["bag"] = bag
            return redirect("bag")

        elif action == "pre_order":
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
