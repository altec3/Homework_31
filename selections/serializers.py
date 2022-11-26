from rest_framework import serializers

from ads.models import Ad
from ads.serializers import AdSerializer
from selections.models import Selection


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionCreateSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Ad.objects.all(),
        slug_field="id"
    )

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = ["id", "name", "items", "owner_id"]


class SelectionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = "__all__"
        read_only_fields = ['owner_id']


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]
