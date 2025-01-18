import logging

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.utils.timezone import now

from .models import Product, Category
from husbandry_system.models import HusbandrySystem
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

    if request.method == "POST":
        action = request.POST.get("action")
        print("DEBUG: action being sent: ", action)

        if action == "add_to_bag":
            print("DEBUG: running add_to_bag logic!")
            bag = request.session.get("bag", {})
            bag[str(product.id)] = bag.get(str(product.id), 0) + 1
            request.session["bag"] = bag
            return redirect("bag")

        elif action == "pre_order":
            print("DEBUG: running pre_order logic!")
            PreOrder.objects.create(
                user=request.user,
                product=product,
                quantity=1,
                date_preordered=now(),
            )
            return redirect("pre_order_confirmation")
    
    context = {
        "product": product,
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
