from django.shortcuts import render
from .models import Users
# Create your views here.
from django.http import HttpResponse

def deshboard(request):
    #user= Users("7raseltrtr@gmail.com", "123er4R")
    #user.save()
    return HttpResponse("hello word!!")