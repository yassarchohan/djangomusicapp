

from rest_framework import serializers

from music.models import Songs


class songserializers(serializers.ModelSerializer):
    class Meta:
            model = Songs
            fields = ("title", "author")