from django.conf.urls import url
from projects.views import (ProjectsListView,
                            NetworkView,
                            TreeView)


urlpatterns = [
    url(r'^$', ProjectsListView.as_view(), name='projects'),
    url(r'^network_graph/$', NetworkView.as_view(), name='network_graph'),
    url(r'^decision_tree/$', TreeView.as_view(), name='decision_tree')
]
