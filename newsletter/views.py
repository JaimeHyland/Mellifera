from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import NewsletterSignupForm
from .models import NewsletterSignup
from django.conf import settings

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            subscriber, created = NewsletterSignup.objects.get_or_create(
            email=form.cleaned_data['email']
            )
            if created or not subscriber.verified:
                # Send verification email
                verification_url = request.build_absolute_uri(
                    f"/verify-newsletter/{subscriber.verification_token}/"
                )
                send_mail(
                    "Verify Your Newsletter Subscription",
                    f"Click the link to verify your subscription: {verification_url}",
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email],
                )
                messages.success(request, "Check your email to verify your subscription.")
            else:
                messages.info(request, "You are already subscribed and verified!")
        else:
            messages.error(request, "Invalid email address. Please try again.")
    else:
        form = NewsletterSignupForm()

    return render(request, "newsletter/newsletter_signup.html", {"form": form})


def verify_subscription(request, token):
    subscriber = get_object_or_404(NewsletterSignup, verification_token=token)
    if not subscriber.verified:
        subscriber.verified = True
        subscriber.save()
        return HttpResponse("Your subscription is verified! Thank you.")
    else:
        return HttpResponse("This subscription is already verified.")
