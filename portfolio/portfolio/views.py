"""Class based views for model-independent information."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class HomeView(TemplateView):
    """View for the homepage."""

    template_name = 'portfolio/home.html'
