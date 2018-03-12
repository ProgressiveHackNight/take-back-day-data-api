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

class DecSerializer(serializers.ModelSerializer):
    location_name = serializers.Field(source='Location')
    street_address = serializers.Field(source='Street Address')
    city = serializers.Field(source='City')
    zip = serializers.Field(source='Zip')
    county = serializers.Field(source='County')
    latitude = serializers.Field(source='Latitude')
    longitude = serializers.Field(source='Longitude')
    type = serializers.Field(source='Type')
    note = serializers.Field(source='Note')
    website = serializers.Field(source='Website')
    class Meta:
        model = Place
        fields = (
            'location_name',
            'street_address',
            'city',
            'zip',
            'county',
            'latitude',
            'longitude',
            'type',
            'note',
            'website',
        )

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

# http://jsatt.com/blog/abusing-django-rest-framework-part-3-object-level-read-only-fields/
class SampleSerializer(serializers.ModelSerializer):

    def get_fields(self, *args, **kwargs):
        self.fields = super(SampleSerializer, self).get_fields(*args, **kwargs)

        # request = self.context.get('request', None)
        # view = self.context.get('view', None)
        #
        # if (request and view and getattr(view, 'object', None) and request.user == view.object.user):
        #     field['is_admin'].read_only = True
        #
        return fields

    class Meta:
        model = Place
        # fields = get_fields()
