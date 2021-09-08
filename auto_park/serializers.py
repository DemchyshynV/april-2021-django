from rest_framework import serializers as s
from car.models import CarModel
from .models import AutoParkModel
from car.serializers import CarSerializer


class AutoParkSerializer(s.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'city', 'cars')


class AutoParkAddCarSerializer(s.ModelSerializer):
    class Meta:
        model = CarModel
        exclude = ('auto_park',)
