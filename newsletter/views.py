from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully signed up for the newsletter!')
        else:
            messages.error(request, 'Please provide a valid email address.')
        return redirect('home')

    # For a GET request, show a blank form
    form = NewsletterSignupForm()
    
    return render(request, 'newsletter/newsletter_signup.html', {'form': form})