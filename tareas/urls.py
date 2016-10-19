from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^crea/', Tarea.as_view(), name='crea'),
]
