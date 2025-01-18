from django.contrib import admin
from .models import PreOrder

@admin.register(PreOrder)
class PreOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'date_preordered')
    list_filter = ('date_preordered',)
    search_fields = ('user__username', 'product__name')
