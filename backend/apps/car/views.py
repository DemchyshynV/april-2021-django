from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from paginations.my_pagination import MyPagination
from permissions.is_superuser import IsSuperUser

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('brand', 'year')

    # def get_queryset(self):
    #     qs = CarModel.objects.all()
    #     pk = self.request.query_params.get('autoParkId')
    #     if pk:
    #         return qs.filter(auto_park_id=pk)
    #     return qs


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
