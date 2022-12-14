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

# ADMIN
def caradmin(request):
    cars_list = Vehicle.objects.all().order_by('-id')

    cars_c = Vehicle.objects.all().count()
    messages_c = Contact.objects.all().count()
    team_c = Team.objects.all().count()
    fback_c = Testimony.objects.all().count()
    blog_c = Blog.objects.all().count()

    page = request.GET.get('page', 1)

    paginator = Paginator(cars_list, 20)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

  

    context = {
        'cars':cars,
        'cars_c':cars_c,
        'messages_c':messages_c,
        'team_c':team_c,
        'fback_c':fback_c,
        'blog_c':blog_c
    }    
    return render(request, 'caradmin/index.html', context)    

def add_car(request):
    form = VehicleForm()
 
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)   
        files = request.FILES.getlist('more_vehicle_images')

        if form.is_valid():  
            vehicle = form.save() 
            for f in files:
                vehicle_image = VehicleImages(vehicle=vehicle, image=f)
                vehicle_image.save()

            return redirect('caradmin')  
    context = {
        'form':form
    }
    return render(request, 'caradmin/form.html', context)        

# edit view -vehicle
# delete view - testimonial, vehicle
def adminblogs(request):
    blogs_list = Blog.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs_list, 12)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs':blogs
    }
    return render(request, 'caradmin/blogs.html', context)

def blog_add(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminblogs')
    context = {
        'form':form
    }
    return render(request, 'caradmin/form.html', context)

def blog_edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('adminblogs')
    context = {
        'blog':blog,
        'form':form
    }
    return render(request, 'caradmin/form.html', context)

def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)   
    blog.delete()
    return redirect('adminblogs') 


def team_edit(request, id):
    team = get_object_or_404(Team, id=id)
    form = TeamForm(instance=team)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('adminteam')
    context = {
        'team':team,
        'form':form
    }
    return render(request, 'caradmin/form.html', context)

def team_delete(request, id):
    team = get_object_or_404(Team, id=id)   
    team.delete()
    return redirect('adminteam') 

def vehicle_delete(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)   
    vehicle.delete()
    return redirect('caradmin')     

def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)   
    contact.delete()
    return redirect('adminfeedback')     

def testimonial_delete(request, id):
    testimonial = get_object_or_404(Testimony, id=id)   
    testimonial.delete()
    return redirect('adminfeedback')     

def car_edit(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(instance=vehicle)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form .is_valid():
            form.save()
            return redirect('caradmin')

    context = {
        'vehicle':vehicle,
        'form':form
    }
    return render(request, 'caradmin/form.html', context)    

def adminteam(request):
    team_list = Team.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(team_list, 12)

    try:
        team = paginator.page(page)
    except PageNotAnInteger:
        team = paginator.page(1)
    except EmptyPage:
        team = paginator.page(paginator.num_pages)
    context = {
        'team':team
    }
    return render(request, 'caradmin/team.html', context)

def team_add(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminteam')
    context = {
        'form':form
    }
    return render(request, 'caradmin/form.html', context)    

def adminfeedback(request):
    testimony_list = Testimony.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(testimony_list, 6)

    try:
        feedback = paginator.page(page)
    except PageNotAnInteger:
        feedback = paginator.page(1)
    except EmptyPage:
        feedback = paginator.page(paginator.num_pages)

    messages_list = Contact.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(messages_list, 6)

    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)

    context = {
        'feedback':feedback,
        'messages':messages
    }
    return render(request, 'caradmin/testimonies.html', context)    