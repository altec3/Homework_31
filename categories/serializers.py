from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        min_length=5,
        max_length=10,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        fields = "__all__"
