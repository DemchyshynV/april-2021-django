from rest_framework import serializers as s

from .models import AutoParkModel
from car.serializers import CarSerializer

class AutoParkSerializer(s.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'city', 'cars')
