from .models import user, userprofile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # userid = serializers.IntegerField()
    first_name = serializers.SerializerMethodField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = userprofile
        fields = [
        'id', 'first_name', 'user', 'last_name', 'job', 'location',
        ]

    # def create(self, validated_data):
    #     s = user.objects.create(first_name = validated_data.get('first_name'), last_name = validated_data.get('last_name'), id = validated_data.get('userid'))
    #     return userprofile.objects.create(job = validated_data.get('job'), user = s, location = validated_data.get('location'))



        #
        # class UserProfileSerializer(serializers.ModelSerializer):
        #     id = serializers.IntegerField(source='user.id')
        #     first_name = serializers.CharField(source='user.first_name')
        #     last_name = serializers.CharField(source='user.last_name')
        #
        #     class Meta:
        #         model = userprofile
        #         fields = [
        #
        #             'id', 'first_name', 'last_name', 'job', 'location']


