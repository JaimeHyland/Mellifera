from django.urls import path
from . import views

urlpatterns = [
    # path('', views.pre_order_view, name='view_pre_order'),
    path('pre-order/confirmation/', views.pre_order_confirmation, name='pre_order_confirmation'),
    path('pre-order/edit/', views.pre_ordered_products, name='edit_pre_orders'),
    path('pre-order/<int:product_id>/', views.pre_order_detail, name='pre_order_detail'),
]