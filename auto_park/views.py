from rest_framework.generics import ListCreateAPIView

from .serializers import AutoParkSerializer
from .models import AutoParkModel


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
