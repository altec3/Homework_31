import pytest


@pytest.mark.django_db(reset_sequences=True)
def test_create_selection(client, token, auth_data):

    user_obj = auth_data["user"]
    user = user_obj.objects.get(username=auth_data["username"])

    request_data = {
        "name": user.username,
        "owner": user.id
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

    assert user.id == 1
    assert response.status_code == 201
    assert response.data == expected_data
