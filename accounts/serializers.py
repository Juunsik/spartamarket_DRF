from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            'password',
            "date_joined",
            "username",
            "email",
            "name",
            "nickname",
            "birth",
            "gender",
            "description",
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "date_joined",
            "username",
            "email",
            "name",
            "nickname",
            "birth",
            "gender",
            "description",
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "nickname",
            "birth",
            "gender",
            "description",
        )
