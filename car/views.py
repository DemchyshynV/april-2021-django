from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CarSerializer
from .models import CarModel
from django.db.models import Q

# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         return self.list(*args, **kwargs)
#
#     def post(self, *args, **kwargs):
#         return self.create(*args, **kwargs)
#
#
# class CarRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         return self.retrieve(*args, **kwargs)
#
#     def put(self, *args, **kwargs):
#         return self.update(*args, **kwargs)
#
#     def patch(self, *args, **kwargs):
#         return self.partial_update(*args, **kwargs)
#
#     def delete(self, *args, **kwargs):
#         return self.destroy(*args, **kwargs)

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    # queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        # rang = self.request.query_params.getlist('rang')
        # if rang:
        #     qs = qs.filter(cost__range=rang)
        # qs = qs.order_by('-id')
        # qs= [qs.last()]
        qs = qs.filter(Q(year=2001) | Q(cost=100))
        return qs


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
