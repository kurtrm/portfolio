"""Class based views for model-independent information."""
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """View for the homepage."""

    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = {'name': 'Kurt Maurer',
                   'about_first': 'This is some text describing Kurt.',
                   'about_second': 'This is osme more text describing Kurt.'}
        return context
