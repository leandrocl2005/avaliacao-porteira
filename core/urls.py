from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^projetos/lista/$', views.projetos_list, name='projetos_list'),
    url(r'^projeto/(?P<pk>\d+)/$', views.projeto_detalhe, name='projeto_detalhe'),
    url(r'^avaliar/(?P<pk>\d+)/$', views.projeto_avaliar, name='projeto_avaliar'),
]