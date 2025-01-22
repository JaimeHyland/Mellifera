from django.db import models
from django.utils.crypto import get_random_string


class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64,  blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.verification_token:
            self.verification_token = get_random_string(64)
        super().save(*args, **kwargs)
