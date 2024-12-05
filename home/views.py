from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from products.models import Product
from husbandry_system.models import HusbandrySystem

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def send_test_email(request):
    try:
        send_mail(
            'Test Email Subject',
            'This is a test email.',
            'hylandjaime@gmail.com',  # Replace with your actual from email
            ['jaime.hyland@language-landscapes.com'],  # Replace with the recipient's email
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def home(request):
    # Get all husbandry systems for the dropdown
    husbandry_systems = HusbandrySystem.objects.all()

    # Get the selected husbandry system from the query parameter (if set)
    selected_husbandry_system = request.GET.get('husbandry_system')

    # If a husbandry system is selected, filter the products
    if selected_husbandry_system:
        # Filter products by the selected husbandry system
        products = Product.objects.filter(husbandry_system_id=selected_husbandry_system) | Product.objects.filter(husbandry_system__isnull=True)
    else:
        # If no filter is selected, show all products
        products = Product.objects.all()

    return render(request, 'home.html', {
        'husbandry_systems': husbandry_systems,
        'selected_husbandry_system': selected_husbandry_system,
        'products': products,
    })

    