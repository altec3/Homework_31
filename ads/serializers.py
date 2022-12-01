from rest_framework import serializers

from ads.models import Ad
from ads.validators import BooleanValueValidator


class AdSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=10
    )

    is_published = serializers.BooleanField(
        validators=[BooleanValueValidator()]
    )

    class Meta:
        model = Ad
        fields = "__all__"
