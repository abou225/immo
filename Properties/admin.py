from django.contrib import admin

# Register your models here.
from Properties.models import Property

# Register your models here.
admin.site.register(Property)

class PropertyAdmin(admin.ModelAdmin):
    # Spécifiez les champs à afficher dans la liste
    list_display = ('name','description','price','superficy','type','address', 'image', 'bedrooms', 'bathrooms')