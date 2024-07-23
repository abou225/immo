from django import forms
from .models import Property

class pForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name','description','price','superficy','type','address', 'image', 'bedrooms', 'bathrooms']