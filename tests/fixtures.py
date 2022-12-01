import pytest


@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = "test"
    password = "123test"

    django_user_model.objects.create_user(
        username=username, password=password
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        content_type='application/json'
    )

    return response.data["access"]
