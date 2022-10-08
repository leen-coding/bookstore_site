
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from arduino.models import IoT
# DB = []
from arduino.views import IoTSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class home(APIView):
    def get(self,request):
        return render(request, 'socketchart.html')