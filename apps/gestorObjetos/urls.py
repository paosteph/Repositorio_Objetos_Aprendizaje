from django.conf.urls import url, include, patterns
from apps.gestorObjetos.views import index, ingresar, principal, privado, categoria, objeto, cerrar


urlpatterns = [

    #url(r'^$', views.post_list),
    url(r'^principal/', principal),
    url(r'^ingresar/', ingresar),
    #url(r'^privado/', privado),
    url(r'^$', index, name='Primera view 3'),
    url(r'^privado/', privado),
    url(r'^categoria/(?P<id_categoria>\d+)$', categoria),
    url(r'^objeto/(?P<id_objeto>\d+)$',objeto),
    url(r'^cerrar/$', cerrar),
]

