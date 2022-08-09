from django import forms
from .models import *


class VehicleForm(forms.ModelForm):
    more_vehicle_images = forms.FileField(
        required=False, widget=forms.FileInput(attrs={
        'class':'form-control',
        'multiple':True
        }))
    class Meta:
        model =Vehicle
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields = '__all__'

class TestimonyForm(forms.ModelForm):
    class Meta:
        model =Testimony
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = '__all__'
