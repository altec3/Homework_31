import pytest


@pytest.fixture
def auth_data(django_user_model):

    return {
        "user": django_user_model,
        "username": "test",
        "password": "test-password"
    }


@pytest.fixture
@pytest.mark.django_db
def token(client, auth_data):

    user_obj = auth_data["user"]

    # Добавим пользователя в базу
    user_obj.objects.create_user(
        username=auth_data["username"],
        password=auth_data["password"]
    )

    response = client.post(
        "/user/token/",
        {"username": auth_data["username"], "password": auth_data["password"]},
        content_type='application/json'
    )

    return response.data["access"]
