from django.urls import path
from . import views

urlpatterns = [
    # path('', views.pre_order_view, name='view_pre_order'),
    path('pre-order/confirmation/', views.pre_order_confirmation, name='pre_order_confirmation'),
    # path('add/<item_id>/', views.add_to_pre_order, name='add_to_pre:pre_order'),
    # path('adjust/<item_id>/', views.adjust_pre_order, name='adjust_pre_order'),
    # path('remove/<item_id>/', views.remove_from_pre_order, name='remove_from_pre_order'),
]