from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'You have updated the number of size {size.upper()} of {product.name} to the {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'You have successfully added size {size.upper()} of {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'You have successfully added size {size.upper()} of {product.name} to your bag')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'You have successfully updated the quantity of the {product.name} item, item {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'You have successfully added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'You have successfully updated size {size.upper()} of {product.name} in item {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'You have successfully removed size {size.upper()} of {product.name} from your bag!')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'You have successfully changed the number of {product.name} items, item {bag(item_id)}.')
        else:
            bag.pop(item_id)
            messages.success(request, f'You have successfully removed {product.name} from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, f'You have successfully removed {size.upper()} of {product.name} from your bag!')
        else:
            bag.pop(item_id)
            messages.success(request, f'You have successfully removed {product.name} from your bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.errir(request, f"An error occurred while attempting to remove item: {e}")
        return HttpResponse(status=500)
