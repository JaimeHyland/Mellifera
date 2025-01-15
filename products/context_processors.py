from husbandry_system.models import HusbandrySystem

def husbandry_system_context(request):
    # Retrieve husbandry systems
    husbandry_systems = HusbandrySystem.objects.values_list('name', flat=True).distinct()

    # Get selected husbandry system from the session or GET parameter
    selected_husbandry_system = request.session.get('husbandry_system', '')

    # Store the selected husbandry so that it persists as long as the current session lasts!
    if selected_husbandry_system:
        request.session['husbandry_system'] = selected_husbandry_system

    return {
        'husbandry_systems': husbandry_systems,
        'selected_husbandry_system': selected_husbandry_system
    }