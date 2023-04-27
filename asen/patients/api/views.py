from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from asen.patients.models import Patient
from asen.patients.api.serializers import PatientSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(detail=True, methods=["get"])
    def toggle_patient_status(self, request, pk=None):
        instance = self.get_object()
        instance.status = "disabled" if instance.status == "active" else "active"
        instance.saved()
        return Response({"meesage": f"You changed the patient status to be {instance.status}"})
