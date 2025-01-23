import logging

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.utils.timezone import now

from .models import Product, Category
from pre_order.models import PreOrder
from .forms import ProductForm


def product_list(request):

    query = None
    categories = None
    sort = None
    direction = None

    selected_husbandry_system = request.session.get('husbandry_system', '')

    if selected_husbandry_system:
        products = Product.objects.filter(
            current=True
            ).filter(
            Q(husbandry_system__name=selected_husbandry_system)| Q(husbandry_system__isnull=True)
        )
    else:
        products = Product.objects.filter(current=True)


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't created any search criteria for your search!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'selected_husbandry_system': selected_husbandry_system,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    pre_ordered_quantity = 0
    pre_order_date = None

    try:
        pre_order = PreOrder.objects.get(user=request.user, product=product)
        pre_ordered_quantity = pre_order.quantity
        pre_order_date = pre_order.date_preordered
    
    except PreOrder.DoesNotExist:
        pre_ordered_quantity = 0
        pre_order_date = None

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "add_to_bag":
            bag = request.session.get("bag", {})
            bag[str(product.id)] = bag.get(str(product.id), 0) + 1
            request.session["bag"] = bag
            
            return redirect("view_bag")

        elif action == "pre_order":
            try:
                quantity = int(request.POST.get("quantity", 1))
                if quantity < 1:
                    raise ValueError("Quantity must be at least 1.")

                # Create a pre_order for the product
                pre_order, created = PreOrder.objects.get_or_create(
                    user=request.user,
                    product=product,
                    defaults={"quantity": quantity, "date_preordered": now()},
                )

                messages.success(request, f"Pre-order updated! Total quantity: {pre_order.quantity}.")
            except ValueError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, "An error occurred while processing your pre-order.")
                
            return redirect('pre_order_confirmation', product_id=product_id)
    
    context = {
        "product": product,
        "pre_ordered_quantity": pre_ordered_quantity,
        "pre_order_date": pre_order_date,
    }
    
    return render(request, "products/product_detail.html", context)
    

@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "This page is only accessible to Mellifera staff.")
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'You have successfully added a new product to the range.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Could not add new product. Please make sure your form entries are valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "This page is only accessible to Mellifera staff.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully modified the product record!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed attempt to update product. Please check that your entries are valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are currently editing {product.name}.')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "This page is only accessible to Mellifera staff.")
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    del_product_name = product.name
    product.delete()
    messages.info(request, f'You have successfully deleted the {del_product_name} product')
    return redirect(reverse('products'))
