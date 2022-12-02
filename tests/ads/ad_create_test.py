import pytest


@pytest.mark.django_db
def test_create_ad(client, token, auth_data):

    user_obj = auth_data["user"]
    user = user_obj.objects.get(username=auth_data["username"])

    request_data = {
        "name": "Temp-name for test",
        "price": 100,
        "description": "",
        "author": user.id
    }

    expected_data = {
        "id": 1,
        "name": request_data["name"],
        "is_published": False,
        "price": request_data["price"],
        "description": request_data["description"],
        "image": None,
        "author": request_data["author"],
        "category": None
    }
    response = client.post(
        "/ad/",
        request_data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token
    )
    assert response.status_code == 201
    assert response.data == expected_data
