from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user.models import User as UserModel

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "password", "fullname", "phone", "email", "is_active", "is_admin", "is_seller"]
        extra_kwargs = {
            'password' : {'write_only':True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        password = make_password(password)
        user = UserModel(**validated_data)
        user.password = password
        user.save()
        return user


class InActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "username", "is_active", "is_seller"]

