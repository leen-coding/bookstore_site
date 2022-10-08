from django.shortcuts import render
from .models import IoT
# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import serializers


class IoTSerializers(serializers.Serializer):
    prime = serializers.IntegerField()
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
    humidity = serializers.DecimalField(max_digits=5, decimal_places=2)


class arduinopost(APIView):

    def get(self, request):
        pass

    def post(self, request):
        request.data["prime"]= IoT.objects.all().__len__()+1
        serializer = IoTSerializers(data=request.data)
        # print(serializer.data)
        if serializer.is_valid():
            #数据校验
            new_data = IoT.objects.create(**serializer.data)
        else:
            return HttpResponse("wrong value")
        # print(request.data)
        return HttpResponse("ok")
