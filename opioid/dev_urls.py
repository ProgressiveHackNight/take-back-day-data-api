from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

import debug_toolbar

from .production_urls import urlpatterns

# Django debug toolbars patterns
urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]

# Staticfiles patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
