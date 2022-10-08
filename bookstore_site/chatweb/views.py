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
        return render(request, 'chart.html')
# def home(request):
#     return render(request, 'chathtml.html')


# def send_msg(request):
#     print(request.GET)
#     text = request.GET.get('text')
#     # DB.append(text)
#
#     return HttpResponse("ok")

class getinfo(APIView):
    def get(self,request):
        index = request.GET.get('index')
        index = int(index)
        print(index)

        new_data_list = IoT.objects.filter(prime__gt=index)
        #long_poll
        while(new_data_list.__len__()==0):
            new_data_list = IoT.objects.filter(prime__gt=index)
        serializer = IoTSerializers(instance=new_data_list, many=True)
        # print(serializer.data.list)
        return Response(serializer.data)


# def get_msg(request):
#     index = request.GET.get('index')
#     index = int(index)
#     new_data_list = IoT.objects.filter(prime__gt=index)
#     serializer = IoTSerializers(instance=new_data_list,many=True)
    # print(serializer.data)
    # serializer.data.append(IoT.objects.all().__len__())
    # context = {
    #     # "data": DB[index:],
    #     # "max_index": len(DB)
    # }
    # data_string = json.dumps(DB)#序列化
    # return JsonResponse(context)
    # return Response(serializer.data)
