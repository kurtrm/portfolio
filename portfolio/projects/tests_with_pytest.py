"""Pytest versions of django unittests."""
import pytest

from django.test import Client
from django.urls import reverse


@pytest.fixture
def client():
    return Client()


def test_200_okay(client):
    """Test that we get a 200 okay."""
    response = client.get(reverse('home'))
    assert response.status_code == 200
