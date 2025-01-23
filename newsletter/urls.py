from django.urls import path
from . import views

urlpatterns = [
    path(
        'newsletter_signup/',
        views.newsletter_signup,
        name='newsletter_signup'
    ),
    path(
        "verify-subscription/<str:token>/",
        views.verify_subscription,
        name="verify_subscription"
    ),
]
