from django.db import models

# Create your models here.


class vehicle(models.Model):
    lp_number = models.CharField(max_length=10, null=False, unique=True)
    wheel_count = models.IntegerField()
    manufacturer = models.CharField(max_length=25, null=False)
    model_name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class car(vehicle):
    is_air_conditioned = models.BooleanField()
    has_roof_top = models.BooleanField()


class truck(vehicle):
    max_goods_weight = models.IntegerField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', default=None)
