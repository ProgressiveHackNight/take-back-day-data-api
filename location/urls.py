from django.conf.urls import url
from location import views


urlpatterns = [
    url(r'^read_json/$', views.read_dec_data_json, name='read-dec-data'),
    url(r'^read_spreadsheet/$', views.read_spreadsheet, name='read-spreadsheet'),
    url(r'^export_places/$', views.export_places, name='export-places'),
]
