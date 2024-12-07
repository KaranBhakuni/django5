from django.urls import path
from app1.views import app1_fun
urlpatterns = [
    path('dj/',app1_fun)
]
