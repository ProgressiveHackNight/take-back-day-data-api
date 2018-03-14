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

class Place(models.Model):

    location_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    street_address = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    city = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    zip = models.CharField(
        max_length=10,
        blank=False,
        null=False,
    )
    borough = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    county = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    hours = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    latitude = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    longitude = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    type = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    note = models.TextField(
        blank=True,
        null=True,
    )
    website = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['county', 'zip']
        unique_together = ('location_name', 'street_address')
