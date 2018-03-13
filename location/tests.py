from django.test import TestCase
from django.conf import settings
import json
from rest_framework.test import APIRequestFactory
from .views import read_dec_data_json, export_places
from .models import Place
import os
import pickle

# Create your tests here.

factory = APIRequestFactory()

class IngestTests(TestCase):

    def setUp(self):
        self.pickle_source = open(os.path.join(settings.MEDIA_ROOT, 'dec_data.p'), 'r')
        self.json_source = os.path.join(settings.MEDIA_ROOT, 'dec_data.json')
        self.json_source_file_object = open(self.json_source, 'r')

    def test_number_of_fields_pickle(self):

        dec_data = pickle.load(self.pickle_source)

        keys = dec_data.keys()

        self.assertEqual(len(keys), 9)

    def test_number_of_fields_json(self):

        request = factory.get('/location/read-dec-data/')
        view = read_dec_data_json(request)
        self.assertEqual(Place.objects.count(), 416)


class ExportTests(TestCase):

    def test_export_all(self):

        request = factory.get('/location/read-dec-data/')
        view = read_dec_data_json(request)
        self.assertEqual(Place.objects.count(), 416)


        request = factory.get(
            'location/export_all/',
        )
        view = export_places(request)
        response=view(request)

        self.assertMultiLineEqual(response.data, {})
