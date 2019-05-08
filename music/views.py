from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from music.models import Songs
from .serializers import songserializers


class ListSongsView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = songserializers

