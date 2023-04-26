from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from asen.patients.models import Patient
from asen.patients.api.serializers import PatientSerializer

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    @action(detail=True, methods=["get"])
    def disable_patient(self, request, pk=None):
        instance = self.get_object()
        if instance.status == "active":
            instance.status = "disabled"
            instance.save()
            return Response({"message": f"Patient status is now {instance.status}."})
        return Response({"message": "Patient already disabled."})