import pytest


@pytest.mark.django_db
def test_can_call_endpoint(client):
    request = client.get(
        '/api/swagger/?format=openapi')
    assert request.status_code == 200
