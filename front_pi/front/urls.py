from django.urls import path
from .views import login, home, clientes, alterar_cliente ,cadastrar_clientes, detalhes_cliente, excluir_cliente, produtos, cadastrar_produtos, error

app_name = 'front'

"""
Urls do app front.
"""

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/<uuid:pk>', detalhes_cliente, name='detalhes_cliente'),
    path('clientes/cadastro/', cadastrar_clientes, name='cadastrar_clientes'),
    path('clientes/delete/<uuid:pk>', excluir_cliente, name='excluir_cliente'),
    path('clientes/alterar/<uuid:pk>', alterar_cliente, name='alterar_cliente'),
    path('produtos/', produtos, name='produtos'),
    path('produtos/cadastro/', cadastrar_produtos, name='cadastrar_produtos'),
    path('error', error, name='erro')
]