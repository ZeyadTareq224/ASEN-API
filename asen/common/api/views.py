from rest_framework.generics import ListAPIView
from asen.common.models import Gender
from asen.common.api.serializers import GenderSerializer

class GenderListView(ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    