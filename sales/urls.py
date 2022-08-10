from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('cars/', cars, name="cars"),
    path('blogs/', blogs, name="blogs"),
    path('feedback/', feedback, name="feedback"),
    path('contact/', contact, name="contact"),
    path('write-testimony/', testimony, name="testimony"),
    path('car/<slug:slug/', car, name="car"),
    path('blog/<slug:slug/', blog, name="blog"),

]