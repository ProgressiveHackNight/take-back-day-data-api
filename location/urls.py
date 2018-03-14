from django.conf.urls import url
from location import views


urlpatterns = [
    url(r'^delete_database/$', views.delete_database, name='delete-database'),
    url(r'^read_json/$', views.read_dec_data_json, name='read-dec-data'),
    url(r'^read_spreadsheet/$', views.read_spreadsheet, name='read-spreadsheet'),
    url(r'^export_json/$', views.export_json, name='export-json'),
    url(r'^export_xlsx/$', views.export_xlsx, name='export-xlsx'),
]
