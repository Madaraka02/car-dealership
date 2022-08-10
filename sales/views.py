from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    # call latest 3 vehicles
    featured_vehiclees = Vehicle.objects.all().order_by('-id')[:3]
    # call latest blogs
    latest_blogs = Blog.objects.all().order_by('-id')[:3]
    # call testimonies - slideshow
    latest_testimonies = Testimony.objects.all().order_by('-id')[:4]

    context = {
        'featured_vehiclees':featured_vehiclees,
        'latest_blogs':latest_blogs,
        'latest_testimonies':latest_testimonies
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def cars(request):
    cars_list = Vehicle.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(cars_list, 6)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    context = {
        'cars':cars
    }
    return render(request, 'cars.html', context)

def blogs(request):
    recent = Blog.objects.all().order_by('-id')[:3]
    blogs_list = Blog.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs_list, 6)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    
    context = {
        'blogs':blogs,
        'recent':recent
    }
    return render(request, 'blog.html', context)

def feedback(request):
    feedback = Testimony.objects.all().order_by('-id')
    
    context = {
        'feedback':feedback,
        # 'form':form
    }
    return render(request, 'testimonials.html', context)



def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={
        'form':form
    }  
    return render(request, 'contact.html', context)      


def testimony(request):
    form = TestimonyForm()
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={
        'form':form
    }  
    return render(request, 'testimony.html', context)   


def car(request, slug):
    car = get_object_or_404(Vehicle, slug=slug)
    context = {
        'car':car
    }
    return render(request, 'car-details.html', context)

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog':blog
    }
    return render(request, 'blog-details.html', context)


def team(request):
    team = Team.objects.all().order_by('-id')
    context = {
        'team':team
    }
    return render(request, 'team.html', context)











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

# admin view
# all vehicles view
# single vehicle view
# single blog view
# contact view
