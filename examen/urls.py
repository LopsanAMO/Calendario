from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
