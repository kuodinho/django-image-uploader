from thumbnails.models import Thumbnails
from thumbnails.serializers import ThumbnailsSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from thumbnails.serializers import UserSerializer
from rest_framework import permissions


class ThumbnailList(generics.ListCreateAPIView):
    queryset = Thumbnails.objects.all()
    serializer_class = ThumbnailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ThumbnailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thumbnails.objects.all()
    serializer_class = ThumbnailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
