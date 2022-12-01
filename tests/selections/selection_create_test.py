import pytest


@pytest.mark.django_db
def test_create_selection(client, token):

    request_data = {
        "name": "test",
        "owner": 1
    }

    expected_data = {
        "id": 1,
        "items": [],
        "name": request_data["name"],
        "owner": request_data["owner"]
    }
    response = client.post(
        "/selection/create/",
        request_data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token
    )
    assert response.status_code == 201
    assert response.data == expected_data
