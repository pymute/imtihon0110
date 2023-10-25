from .models import CustomUser
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class CustomUserSerializer(ModelSerializer):

    def create(self, validated_date):
        user = CustomUser(
            username=validated_date['username'],
            # first_name = validated_date.get('first_name'),
            # phone = validated_date.get('phone'),
            role=validated_date.get('role',1)
        )
        user.set_password(validated_date['password'])
        user.save()
        return user
    class Meta:
        model = CustomUser
        fields = ('username', 'password','role')