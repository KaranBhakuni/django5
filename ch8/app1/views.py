from django.shortcuts import render

# Create your views here.
def app1_fun(req):
    return render(req,'app1/django.html')
