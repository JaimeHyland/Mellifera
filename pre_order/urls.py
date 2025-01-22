from django.urls import path
from . import views

urlpatterns = [
    path('pre-order/confirmation/<int:product_id>/', views.pre_order_confirmation, name='pre_order_confirmation'),
    path('pre-order/edit/', views.pre_ordered_products, name='edit_pre_orders'),
    path('pre-order/<int:product_id>/', views.pre_order_detail, name='pre_order_detail'),
    path('change-pre-order/<int:product_id>/', views.change_pre_order_quantity, name='change_pre_order_quantity'),
    path('delete-pre-order/<int:product_id>/', views.delete_pre_order, name='delete_pre_order'),
]