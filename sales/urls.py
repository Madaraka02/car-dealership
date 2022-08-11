from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name="home"),
    path('about/', about, name="about"),
    path('team/', team, name="team"),
    path('cars/', cars, name="cars"),
    path('blogs/', blogs, name="blogs"),
    path('feedback/', feedback, name="feedback"),
    path('contact/', contact, name="contact"),
    path('write-testimony/', testimony, name="testimony"),
    path('car/<slug:slug>/', car, name="car"),
    path('blog/<slug:slug>/', blog, name="blog"),
    path('cars/admin/', caradmin, name="caradmin"),
    path('cars/admin/blogs/', adminblogs, name="adminblogs"),
    path('cars/admin/team/', adminteam, name="adminteam"),
    path('cars/admin/feeback/', adminfeedback, name="adminfeedback"),

    path('blog/<int:id>/edit/', blog_edit, name="blog_edit"),
    path('team/<int:id>/edit/', team_edit, name="team_edit"),
    path('car/<int:id>/edit/', car_edit, name="car_edit"),
    path('add-car/', add_car, name="add_car"),
    path('add-blog/', blog_add, name="add_blog"),
    path('add-team/', team_add, name="team_add"),



    path('blog/<int:id>/delete/', blog_delete, name="blog_delete"),
    path('team/<int:id>/delete/', team_delete, name="team_delete"),
    path('vehicle/<int:id>/delete/', vehicle_delete, name="vehicle_delete"),
    path('contact/<int:id>/delete/', contact_delete, name="contact_delete"),
    path('testimonial/<int:id>/delete/', testimonial_delete, name="testimonial_delete"),


]