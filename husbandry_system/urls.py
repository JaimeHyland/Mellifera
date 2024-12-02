from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_husbandry_system, name='view_husbandry'),
]