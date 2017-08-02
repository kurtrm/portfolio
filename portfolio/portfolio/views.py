"""Class based views for model-independent information."""
from portfolio.forms import AboutMe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class AboutView(FormView):
    """Form view for about me page."""

    template_name = 'portfolio/about.html'
    form_class = AboutMe
    success_url = 'about'


class HomeView(TemplateView):
    """View for the homepage."""

    pass
