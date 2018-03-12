from django.contrib import admin
from .models import Place

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):

    def get_list_display_links(self, request, list_display):
        # if request.user.is_superuser:
        #     if self.list_display_links or not list_display:
        #         return self.list_display_links
        #     else:
        #         # Use only the first item in list_display as link
        #         return list(list_display)[:1]
        # else:
        #     # Ensures that no hyperlinks appear in the change list for non-superusers
        self.list_display_links = (None, )
        return self.list_display_links


    fields = [
        'location_name',
        'street_address',
        'city',
        'zip',
        'borough',
        'county',
        'phone',
        'hours',
        'latitude',
        'longitude',
        'type',
        'note',
        'website',
        ]

    list_display = [
        'location_name',
        'street_address',
        'city',
        'zip',
        'borough',
        'county',
        'phone',
        'hours',
        'latitude',
        'longitude',
        'type',
        'note',
        'website',
        ]
    search_fields = [
                'location_name',
                'street_address',
                'city',
                'zip',
                'borough',
                'county',
                'phone',
                'hours',
                'latitude',
                'longitude',
                'type',
                'note',
                'website',

    ]


admin.site.register(Place, PlaceAdmin)
