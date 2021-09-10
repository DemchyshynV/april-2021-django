from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from permissions.is_superuser import IsSuperUser

class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        qs = CarModel.objects.all()
        pk = self.request.query_params.get('autoParkId')
        if pk:
            return qs.filter(auto_park_id=pk)
        return qs


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
