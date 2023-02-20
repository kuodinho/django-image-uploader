from rest_framework import serializers
from .models import Thumbnails
from django.contrib.auth.models import User


class ThumbnailsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Thumbnails
        fields = ['created', 'title', 'image', 'id', 'owner']


class UserSerializer(serializers.ModelSerializer):
    thumbnails = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Thumbnails.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'thumbnails']
