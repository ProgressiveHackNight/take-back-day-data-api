import json
import os
from django.shortcuts import redirect
from django.conf import settings
from django.db.utils import IntegrityError
from rest_framework.response import Response
from rest_framework import generics
from .models import Place


def read_dec_data_json(request):

    json_source = os.path.join(settings.MEDIA_ROOT, 'dec_data.json')
    json_source_file_object = open(json_source, 'r')

    dec_data = json.loads(json_source_file_object.read())

    fieldmap = {
            'Location':'location_name',
            'Street Address': 'street_address',
            'City': 'city',
            'Zip': 'zip',
            'County': 'county',
            'Latitude': 'latitude',
            'Longitude': 'longitude',
            'Type': 'type',
            'Note': 'note',
            'tr>Note': 'note',
            'Website': 'website',
            'Hours': 'hours',
            'Phone': 'phone',
            'Borough': 'borough',
            }


    for item in dec_data:
        fields = {}
        # Initialize by setting an empty string to all fields.
        for field in fieldmap:
            fields[fieldmap[field]] = ''

        # Map the current value of the field to the database field
        for key in item:
            fieldname = fieldmap[key]
            fields[fieldname] = item[key]

        # Create objects in database.
        try:

            Place.objects.create(
                location_name=fields['location_name'],
                street_address=fields['street_address'],
                city=fields['city'],
                zip=fields['zip'],
                borough=fields['borough'],
                county=fields['county'],
                phone=fields['phone'],
                hours=fields['hours'],
                latitude=fields['latitude'],
                longitude=fields['longitude'],
                type=fields['type'],
                note=fields['note'],
                website=fields['website'],
            )

        except IntegrityError:
            # It's already there.
            pass

    return redirect('/admin/location/place/')

def export_places(request):

    OUTFILE = os.path.join(settings.MEDIA_ROOT , 'output.json')

    places = Place.objects.all()
    places_as_dict = [
        {
            'location_name': p.location_name,
            'city': p.city,
            'latitude': p.latitude,
            'longitude': p.longitude
        }
        for p in places]

    with open(OUTFILE, 'w') as f:
        json.dump(places_as_dict, f, indent=2)

    return redirect('/media/output.json')
