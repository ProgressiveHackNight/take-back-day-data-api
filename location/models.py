from django.db import models

# Create your models here.

"""
Name
Type
location
city
zip
latitude
longitude
"""

class Item(models.Model):

    typeChoice

    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField()
