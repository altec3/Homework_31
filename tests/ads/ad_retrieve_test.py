import pytest


@pytest.mark.django_db
def test_ad_retrieve(client, ad, token):

    expected_data = {
        "id": ad.pk,
        "name": ad.name,
        "is_published": ad.is_published,
        "price": ad.price,
        "description": ad.description,
        "image": None,
        "author": ad.author_id,
        "category": None
        }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 200
    assert response.data == expected_data
