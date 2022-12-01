from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from locations.models import Location
from users.models import User
from users.validators import UserAgeValidator, EmailDomainValidator


class UserListSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "role", "age", "birth_date", "total_ads", "location_id"]


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location_id = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    birth_date = serializers.DateField(
        validators=[UserAgeValidator(min_age=9)]
    )

    email = serializers.EmailField(
        validators=[
            EmailDomainValidator(domain="rambler.ru"),
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user


class UserRetrieveSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )
    username = serializers.CharField(max_length=20, read_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "role", "age", "birth_date", "location_id"]

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location_id", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location_id.add(location_obj)
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
