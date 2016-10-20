from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^examen/', ExamenView.as_view(), name='examenview'),
]
