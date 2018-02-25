from django.urls import path
from projects.views import (ProjectsListView,
                            NetworkView,
                            TreeView)


urlpatterns = [
    path('', ProjectsListView.as_view(), name='projects'),
    path('network_graph/', NetworkView.as_view(), name='network_graph'),
    path('decision_tree/', TreeView.as_view(), name='decision_tree')
]
