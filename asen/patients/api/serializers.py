from rest_framework import serializers

from django.contrib.auth import get_user_model

from asen.patients.models import Patient
from asen.users.api.serializers import UserSerializer


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "last_login", "date_joined", "name", "email"]


class PatientSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = Patient
        fields = "__all__"
