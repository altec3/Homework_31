from rest_framework import serializers


class BooleanValueValidator:
    def __init__(self, boolean: bool = True):
        self.boolean = boolean

    def __call__(self, value: bool):
        if value == self.boolean:
            raise serializers.ValidationError(f"Value must be '{not value}' only.")
