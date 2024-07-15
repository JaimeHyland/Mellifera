from django.shortcuts import render

# Create your views here.

def view_bag(request):
    print("View Bag function called")  # Debug print statement
    return render(request, 'bag/bag.html')