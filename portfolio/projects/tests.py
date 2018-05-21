from django.test import TestCase, Client
from django.urls import reverse
import bs4


class TestHomeView(TestCase):
    """Tests for the homeview."""

    def setUp(self):
        """Instantiate a client object."""
        self.client = Client()

    def test_network_200_ok(self):
        """Test that we get 200 response."""
        response = self.client.get(reverse('network_graph'))
        self.assertTrue(response.status_code == 200)

    def test_decision_tree_page_200(self):
        """Test that we get 200 response."""
        response = self.client.get(reverse('decision_tree'))
        self.assertTrue(response.status_code == 200)
