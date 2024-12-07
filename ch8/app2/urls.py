from django.urls import path
from app2.views import app2_fun

urlpatterns = [
    path('fastapi/',app2_fun)
    
]
