from django.test import TestCase, Client
from django.urls import reverse


class TestHomeView(TestCase):
    """Tests for the homeview."""

    def setUp(self):
        """Instantiate a client object."""
        self.client = Client()

    def test_200_ok(self):
        """Test that we get 200 response."""
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code == 200)
