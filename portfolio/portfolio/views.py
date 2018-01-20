"""Class based views for model-independent information."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class AboutView(TemplateView):
    """Form view for about me page."""

    template_name = 'portfolio/about.html'
    success_url = 'about'


class HomeView(TemplateView):
    """View for the homepage."""

    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = {'test': 'Test string.'}
        return context
