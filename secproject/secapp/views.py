from rest_framework import viewsets
from .models import user

from . import serializer


class userviewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = serializer.UserSerializer
