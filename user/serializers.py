from django.contrib.auth import get_user_model

from rest_framework import serializers as s

from .models import CustomUser

UserModel: CustomUser = get_user_model()


class UserSerializer(s.ModelSerializer):
    # password = s.CharField(max_length=50, write_only=True)
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
