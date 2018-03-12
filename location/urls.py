from django.conf.urls import url
from location import views


urlpatterns = [
    url(r'^read_json/$', views.read_dec_data_json, name='read-dec-data'),
]
