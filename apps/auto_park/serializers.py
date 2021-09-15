from rest_framework import serializers as s

from apps.car.models import CarModel
from apps.car.serializers import CarSerializer

from .models import AutoParkModel


class AutoParkSerializer(s.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'city', 'cars')


class AutoParkAddCarSerializer(s.ModelSerializer):
    class Meta:
        model = CarModel
        exclude = ('auto_park',)
