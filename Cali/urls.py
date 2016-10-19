from django.conf.urls import url, include
from django.contrib import admin
from usuarios import urls as Userls
from semestre import urls as Semeurls
from materias import urls as Mateurls
from tareas import urls as Tareaurls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuarios/', include(Userls, namespace='usuario')),
    url(r'^semestre/', include(Semeurls, namespace='semestre')),
    url(r'^materia/', include(Mateurls, namespace='materias')),
    url(r'^tarea/', include(Tareaurls, namespace='tareas'))
]
