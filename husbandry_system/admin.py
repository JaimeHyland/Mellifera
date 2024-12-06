from django.contrib import admin
from .models import HusbandrySystem


class HusbandrySystemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'box_length_mm',
        'box_width_mm',
        'depth_deep_mm',
        'depth_medium_mm',
        'depth_shallow_mm',
        'description',
    )


admin.site.register(HusbandrySystem, HusbandrySystemAdmin)
