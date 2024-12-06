from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


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
