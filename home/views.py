from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from husbandry_system.models import HusbandrySystem
from products.models import Product

from django.shortcuts import redirect


def set_husbandry_system(request):
    if request.method == 'POST':
        selected_system = request.POST.get('husbandry_system', '')
        if selected_system:
            request.session['husbandry_system'] = selected_system
        else:
            request.session.pop('husbandry_system', None)  # Clear the filter if no selection
    return redirect(request.META.get('HTTP_REFERER', 'home:index'))

def index(request):
    return render(request, 'home/index.html')


def send_test_email(request):
    try:
        send_mail(
            'Test Email Subject',
            'This is a test email.',
            'hylandjaime@gmail.com',
            ['jaime.hyland@language-landscapes.com'],
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def newsletter_signup(request):
    return render(request, 'newsletter_signup.html')
