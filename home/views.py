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

    