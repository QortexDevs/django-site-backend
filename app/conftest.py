from django.contrib.auth import get_user_model
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def create_new_user():
    user = get_user_model()
    user_created = user.objects.create_user(
        email='email@mail.com', password='password')
    return user_created


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def client(create_new_user, api_client):
    api_client.force_authenticate(user=create_new_user)
    yield api_client
    api_client.force_authenticate(user=None)
