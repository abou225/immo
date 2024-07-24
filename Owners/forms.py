from django import forms
from .models import Owner

class oForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['firstname','lastname','email','phone','address']