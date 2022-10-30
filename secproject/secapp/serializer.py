from .models import user
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [
            "id", "first_name", "last_name", "email"
        ]
