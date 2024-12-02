from rest_framework import serializers
from .models import Hymn
from django.contrib.auth import get_user_model

User = get_user_model()

class HymnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hymn
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_admin')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user