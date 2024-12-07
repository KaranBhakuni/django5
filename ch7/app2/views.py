from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfun2(req):
    return HttpResponse("hello from app2")