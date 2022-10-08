from django.shortcuts import render
from bookstore.models import books
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
def arduinopost(request):
    # print(request.headers)
    if request.method == 'GET':
        return HttpResponse("A")
    if request.method == 'POST':
        var = request.POST
        print(var)
        return HttpResponse("ok")