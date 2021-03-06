import json
import os
import sys
from collections import OrderedDict
from pyexcel_xlsx import get_data, save_data
from django.shortcuts import redirect
from django.conf import settings
from django.db.utils import IntegrityError, DataError
from .models import Place


def delete_database(request):
    places = Place.objects.all()
    places.delete()
    return redirect('/admin/location/place/')


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
        except DataError:
            print('DATA ERROR for item=', item)
            sys.exit()

    return redirect('/admin/location/place/')


def read_spreadsheet(request):
    spreadsheet_filename = os.path.join(settings.MEDIA_ROOT, 'NYS Drop Box Locations 2017-01-31.xlsx')
    data = get_data(spreadsheet_filename)

    datadict = {}
    i = 0
    for sheet in data.keys():
        print('DEBUG ', data[sheet][0])
        for item in data[sheet]:
            i += 1
            print('\tDEBUG item=', item)
            datadict[i] = {
                'location_name': item[0],
                'street_address': item[1],
                'city': item[2],
                'zip': item[3],
                'borough': item[4],
                'county': item[5]
            }
            Place.objects.create(
                location_name=item[0],
                street_address=item[1],
                city=item[2],
                zip=item[3],
                borough=item[4],
                county=item[5],

            )
    print('DEBUG datadict={}'.format(datadict))

    return redirect('/admin/location/place/')

def export_places(request):

    # dump JSON file in media directory and display in browser

    OUTFILE = os.path.join(settings.MEDIA_ROOT , 'output.json')

    places = Place.objects.all()
    places_as_dict = [
        {
            'name': '{}'.format(p.location_name),
            'address': '{}, {}, {}, NY'.format(
                p.street_address,
                p.city,
                p.zip
                ),
            'type': p.type,
            'latitude': p.latitude,
            'longitude': p.longitude,
            'hours': p.hours,
            'notes': p.note,
        }
        for p in places]

    with open(OUTFILE, 'w') as f:
        json.dump(places_as_dict, f, indent=2)

    return redirect('/media/output.json')


def export_xlsx(request):

    # dump database into spreadsheet

    OUTFILE = os.path.join(settings.MEDIA_ROOT , 'output.xlsx')

    data = OrderedDict()
    places = Place.objects.all()
    data_list = [
        [
            p.location_name,
            p.street_address,
            p.city,
            p.zip,
            p.borough,
            p.county,
            p.phone,
            p.hours,
            p.type,
            p.latitude,
            p.longitude,
            p.hours,
            p.note,
            p.website
        ]
    for p in places]

    data_list.insert(0, [
        'LOCATION',
        'STREET ADDRESS',
        'CITY',
        'ZIP',
        'BOROUGH',
        'COUNTY',
        'PHONE',
        'HOURS',
        'TYPE',
        'LATITUDE',
        'LONGITUDE',
        'HOURS',
        'NOTE',
        'WEBSITE'
    ])

    print(data_list)

    data.update({'Sheet 1': data_list })

    save_data(OUTFILE, data)

    return redirect('/media/output.xlsx')
