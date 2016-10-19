from django.conf.urls import url, include
from django.contrib import admin
from usuarios import urls as Userls
from semestre import urlsas as Semeurls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuarios/', include(Userls, namespace='usuario')),
    url(r'^semestre/', include(Semeurls, namespace='semestre')),
]
