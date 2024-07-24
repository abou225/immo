from django.db import models

# Create your models here.

class Property(models.Model):
    
    TYPE_CHOICES = [
        ('villa', 'Villa'),
        ('appartement', 'Appartement'),
        ('store', 'Store'),
    ]

    name = models.CharField(max_length=30)  # name VARCHAR(30) NOT NULL
    description = models.TextField()         # Changed to TextField for better handling of longer text
    price = models.PositiveIntegerField()    # price INT UNSIGNED NOT NULL
    superficy = models.PositiveIntegerField()  # superficy INT UNSIGNED NOT NULL
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)  # Choices for type
    address = models.CharField(max_length=50)  # Corrected spelling and VARCHAR(50) NOT NULL
    image = models.ImageField(upload_to='img')  # Changed upload_to to save images in a 'properties' folder
    bedrooms = models.PositiveSmallIntegerField()  # PositiveSmallIntegerField() does not need max_length
    bathrooms = models.PositiveSmallIntegerField()  # PositiveSmallIntegerField() does not need max_length
    #owner_id = models.ForeignKey("Owner")

    def __str__(self):
        return self.name

    
