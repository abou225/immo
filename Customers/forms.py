from django import forms
from .models import Customer

class cForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname','lastname','email','phone','job','birthday']