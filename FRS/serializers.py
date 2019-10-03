from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.validators import UniqueValidator
from FRS.models import Flight
from django.contrib.auth.models import User


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[
        UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class FlightSerializer(serializers.ModelSerializer):
    """ map model instance to json"""

    class Meta:
        model = Flight
        fields = ['name', 'number', 'scheduled_date',
                  'departure', 'destination', 'fare', 'duration']
