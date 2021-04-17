from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('user', views.UserView.as_view()),
    path('logout',views.LogoutView.as_view()),
    url(r'^proyecto$', views.ProyectoList.as_view()),
    url(r'^proyecto/(?P<pk>[0-9]+)$', views.ProyectoDetail.as_view()),

    url(r'^proyecto-tecnologia$', views.ProyectoTecnologiaList.as_view()),
    url(r'^proyecto-tecnologia/(?P<pk>[0-9]+)$', views.ProyectoTecnologiaDetail.as_view()),

    url(r'^recurso$', views.RecursoList.as_view()),
    url(r'^recurso/(?P<pk>[0-9]+)$', views.RecursoDetail.as_view()),

    url(r'^tecnologia$', views.TecnologiaList.as_view()),
    url(r'^tecnologia/(?P<pk>[0-9]+)$', views.TecnologiaDetail.as_view()),

    url(r'^usuario$', views.UsuarioList.as_view()),
    url(r'^usuario/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),

    url(r'^usuario-tecnologia$', views.UsuarioTecnologiaList.as_view()),
    url(r'^usuario-tecnologia/(?P<pk>[0-9]+)$', views.UsuarioTecnologiaDetail.as_view()),

]