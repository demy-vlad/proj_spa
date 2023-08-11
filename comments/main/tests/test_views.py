import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_index_view_with_empty_form():
    client = Client()
    response = client.post(reverse('index'))

    assert response.status_code == 200
    assert b"All fields are required." in response.content