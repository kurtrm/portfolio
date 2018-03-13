from django.test import TestCase, Client
from django.urls import reverse
import bs4


class TestHomeView(TestCase):
    """Tests for the homeview."""

    def setUp(self):
        """Instantiate a client object."""
        self.client = Client()

    def test_home_200_ok(self):
        """Test that we get 200 response."""
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code == 200)

    def test_about_page_200(self):
        """Test that we get 200 response."""
        response = self.client.get(reverse('about'))
        self.assertTrue(response.status_code == 200)
