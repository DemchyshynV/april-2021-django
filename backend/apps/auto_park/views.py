from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, get_object_or_404

from apps.car.models import CarModel

from .models import AutoParkModel
from .serializers import AutoParkAddCarSerializer, AutoParkSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='list of cars', operation_summary='get method'))
class AutoParkListCreateView(ListCreateAPIView):
    """
    get:
        Выводит список автопарков
    post:
        Создание нового автопарка
    """
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkCarListCreateView(ListCreateAPIView):
    serializer_class = AutoParkAddCarSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return CarModel.objects.filter(auto_park=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        auto_park = get_object_or_404(AutoParkModel, pk=pk)
        serializer.save(auto_park=auto_park)
