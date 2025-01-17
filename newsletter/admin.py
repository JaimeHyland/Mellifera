from django.contrib import admin
from .models import NewsletterSignup

class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)

admin.site.register(NewsletterSignup, NewsletterSignupAdmin)
