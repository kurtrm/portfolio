"""Class based views for model-independent information."""
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """View for the homepage."""

    template_name = 'portfolio/home.html'


class AboutView(TemplateView):
    """View for the about me section."""

    template_name = 'portfolio/about.html'
