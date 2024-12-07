from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfun(req):
    return HttpResponse("hello")