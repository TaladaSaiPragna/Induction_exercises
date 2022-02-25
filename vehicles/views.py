from django.shortcuts import render
from django.http import HttpResponse
from .models import car, truck, vehicle
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import carSerializer, vehicleSerializer, truckSerializer


# Create your views here.
class result(APIView):
    def get(self, request):
        all_cars = car.objects.all()
        all_trucks = truck.objects.all()
        all_vehicles = vehicle.objects.all()
        cars = carSerializer(all_cars, many=True)
        trucks = truckSerializer(all_trucks, many=True)
        vehicles = vehicleSerializer(all_vehicles, many=True)
        res = {
            'cars': cars.data,
            'truck': trucks.data,
            'vehicles': vehicles.data
        }
        return Response(res)
