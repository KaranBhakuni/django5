from django.shortcuts import render

# Create your views here.
def app2_fun(req):
    return render(req,'app2/fastapi.html')
