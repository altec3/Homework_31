from datetime import date

from rest_framework import serializers


class UserAgeValidator:
    def __init__(self, min_age: int = 18):
        self.min_age = min_age

    def __call__(self, birth_date: date):
        today = date.today()
        user_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if user_age < self.min_age:
            raise serializers.ValidationError(f"User age must be at least {self.min_age} years")


class EmailDomainValidator:
    def __init__(self, domain: str):
        self.domain = "@" + domain

    def __call__(self, value: str):
        if self.domain in value:
            raise serializers.ValidationError(
                f"Registration from an email address in the '{self.domain[1:]}' domain is prohibited"
            )
