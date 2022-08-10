from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = AutoSlugField(populate_from='name',null=True)
    condition = models.CharField(max_length=100, null=True, blank=True)
    make = models.CharField(max_length=100, null=True, blank=True)
    vehicle_type = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=200, decimal_places=2, null=True, blank=True)
    mileage = models.CharField(max_length=100, null=True, blank=True)
    engine_size = models.CharField(max_length=100, null=True, blank=True)
    power = models.CharField(max_length=100, null=True, blank=True)
    fuel = models.CharField(max_length=100, null=True, blank=True)
    gearbox = models.CharField(max_length=100, null=True, blank=True)
    doors = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    number_of_seats = models.CharField(max_length=100, null=True, blank=True)
    additional_description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='cars/images', null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 



    def __str__(self):
        return f"{self.name} - {self.make}"

class VehicleImages(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=False)
    image = models.FileField(upload_to='cars/images', null=True, blank=True)
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

    def __str__(self):
        return self.vehicle.name     

class Blog(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='cars/images', null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    snippet = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


    def __str__(self):
        return self.title        

class Testimony(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)   

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField(max_length=300, null=True, blank=True)   
    subject = models.CharField(max_length=300, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email     

class Team(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='cars/images', null=True, blank=True)
    department = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    facebook = models.URLField(max_length=200,null=True, blank=True)
    instagram = models.URLField(max_length=200,null=True, blank=True)
    linkedin = models.URLField(max_length=200,null=True, blank=True)
    twitter = models.URLField(max_length=200,null=True, blank=True)



    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


    def __str__(self):
        return self.name 

