from rest_framework.serializers import ModelSerializer
from asen.patients.models import Patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'