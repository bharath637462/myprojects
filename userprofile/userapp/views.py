from rest_framework import viewsets
from .models import  user

from . import serializers


class userviewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = serializers.UserSerializer
