from django.conf.urls import url
from location import views
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^help/$', TemplateView.as_view(template_name='help.html')),
    url(r'^delete_database/$', views.delete_database, name='delete-database'),
    url(r'^read_json/$', views.read_dec_data_json, name='read-dec-data'),
    url(r'^read_spreadsheet/$', views.read_spreadsheet, name='read-spreadsheet'),
    url(r'^export_places/$', views.export_places, name='export-places'),
    url(r'^export_xlsx/$', views.export_xlsx, name='export-xlsx'),
]
