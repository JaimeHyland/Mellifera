from django.shortcuts import render
from .models import HusbandrySystem

def view_husbandry_system(request):
    systems = HusbandrySystem.objects.all()  # Fetch all HusbandrySystem objects
    return render(request, 'husbandry_system/system_list.html', {'systems': systems})

