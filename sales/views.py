from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_vehicle(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)   
        files = request.FILES.getlist('more_vehicle_images')

        if form.is_valid():  
            vehicle = form.save() 
            for f in files:
                vehicle_image = VehicleImages(vehicle=vehicle, image=f)
                vehicle_image.save()

            return redirect('admin')    