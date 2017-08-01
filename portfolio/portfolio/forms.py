"""Form for the about me that is not bound by a model."""
from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class AboutMe(forms.Form):
    """Form for the about me section."""
    content = forms.CharField(widget=MarkdownWidget())
    content2 = MarkdownFormField()
