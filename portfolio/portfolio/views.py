"""Class based views for model-independent information."""
from forms import AboutMe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView


class AboutView(LoginRequiredMixin, FormView):
    """Form view for about me page."""
    template_name = 'about.html'
    form_class = AboutMe
    success_url = 'about'

    def form_valid(self, form):
        """
