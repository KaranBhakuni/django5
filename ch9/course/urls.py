from django.urls import path
from course.views import learn_django,learn_second
urlpatterns = [
    path('dj/', learn_django),
    path('second/',learn_second),
]
