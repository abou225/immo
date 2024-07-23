from django.contrib import admin
from Customers.models import Customer

# Register your models here.
admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    # Spécifiez les champs à afficher dans la liste
    list_display = ('firstname', 'lastname', 'email', 'phone', 'job', 'birthday')