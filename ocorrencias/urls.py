from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path(
        'registrar/',
        views.criar_ocorrencia,
        name='criar_ocorrencia'
    ),

    path(
        'sucesso/',
        views.sucesso,
        name='sucesso'
    ),

    path(
        'ocorrencias/',
        views.acompanhar_ocorrencias,
        name='acompanhar_ocorrencias'
    ),

    # LOGIN
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='ocorrencias/login.html'
        ),
        name='login'
    ),

    # LOGOUT
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='inicio'
        ),
        name='logout'
    ),

    # PAINEL ADMINISTRATIVO
    path(
        'painel/',
        views.listar_ocorrencias,
        name='listar_ocorrencias'
    ),

    path(
        'painel/editar/<int:id>/',
        views.editar_ocorrencia,
        name='editar_ocorrencia'
    ),

    path(
        'painel/excluir/<int:id>/',
        views.excluir_ocorrencia,
        name='excluir_ocorrencia'
    ),
]