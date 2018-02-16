from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from projects.views import (NetworkView,
                            TreeView)


urlpatterns = [
    url(r'^network_graph/$', NetworkView.as_view(), name='network_graph'),
    url(r'^decision_tree/$', TreeView.as_view(), name='decision_tree')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
