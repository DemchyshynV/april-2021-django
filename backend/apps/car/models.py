from datetime import datetime

from django.core import validators as v
from django.db import models

from apps.auto_park.models import AutoParkModel


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ('id',)

    brand = models.CharField(max_length=255, verbose_name='Бренд', unique=True, validators=[
        v.MinLengthValidator(3),
        v.RegexValidator('^[a-z]+$', 'brand must be only lower alpha characters')
    ])
    year = models.IntegerField(blank=True, default=0, validators=[
        v.MinValueValidator(2000),
        v.MaxValueValidator(datetime.now().year)
    ])  # """null=True"""
    cost = models.IntegerField(validators=[
        v.MinValueValidator(1)
    ])

    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.brand
