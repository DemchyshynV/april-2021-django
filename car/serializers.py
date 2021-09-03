from rest_framework import serializers as s

from .models import CarModel


class CarSerializer(s.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        # fields = ('id', 'brand')
        # exclude = ('id',)

    def validate(self, validate_data:dict):
        year = validate_data.get('year')
        cost = validate_data.get('cost')
        if year == cost:
            raise s.ValidationError('Error, year is equal to cost')
        return validate_data

    def validate_year(self, year):
        if year == 2008:
            raise s.ValidationError('Error')
        return year
