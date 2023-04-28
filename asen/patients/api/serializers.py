from rest_framework import serializers

from django.contrib.auth import get_user_model

from asen.patients.models import Patient
from asen.users.api.serializers import UserSerializer


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = "__all__"
