"""Form for the about me that is not bound by a model."""
from django import forms
from django_markdown.fields import MarkdownFormField


class AboutMe(forms.Form):
    """Form for the about me section."""
    content2 = MarkdownFormField()
