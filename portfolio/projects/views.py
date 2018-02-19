from django.views.generic.base import TemplateView


class ProjectsListView(TemplateView):
    """
    Sticking with TemplateView as no database is required right now.
    """

    template_name = 'projects/projects.html'


class NetworkView(TemplateView):
    """View for the network graph."""

    template_name = 'projects/network.html'


class TreeView(TemplateView):
    """View for the decision tree."""

    template_name = 'projects/decision_tree.html'
