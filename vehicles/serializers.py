from rest_framework import serializers
from .models import vehicle, car, truck


class truckSerializer(serializers.ModelSerializer):
    class Meta:
        model = truck
        fields = '__all__'


class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = '__all__'


class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'
