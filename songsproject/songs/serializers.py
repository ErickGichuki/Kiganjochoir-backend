from rest_framework import serializers
from .models import RecordedSongs, Songs

class RecordedSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedSongs
        fields = '__all__'

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'