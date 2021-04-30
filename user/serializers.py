from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User, Profile


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    @staticmethod
    def validate_password(password):
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 symbols!")
        return password


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']
