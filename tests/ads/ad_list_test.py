import pytest

from tests.factories import AdFactory

from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_ad_list(client):
    ads = AdFactory.create_batch(5)

    expected_data = {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdSerializer(ads, many=True).data
    }

    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_data
