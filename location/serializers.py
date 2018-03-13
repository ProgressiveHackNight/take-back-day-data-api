from rest_framework import serializers
from .models import Place

"""
DEC DATA:

location
street_address
city
zip
county
latitude
longitude
type
notes
website

SPREADSHEET:

location
street_address
city
zip
borough
county

"""

class SpreadsheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'location_name',
            'street_address',
            'city',
            'zip',
            'borough',
            'county',
        )
