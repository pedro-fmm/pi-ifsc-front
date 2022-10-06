from django.urls import path
from .views import login, home
from .views import clientes, alterar_cliente ,cadastrar_clientes, detalhes_cliente, excluir_cliente
from .views import produtos, cadastrar_produtos
from .views import vendas, vendas_adicionar_produto

app_name = 'front'

"""
Urls do app front.
"""

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),

    # Clientes

    path('clientes/', clientes, name='clientes'),
    path('clientes/<uuid:pk>', detalhes_cliente, name='detalhes_cliente'),
    path('clientes/cadastro/', cadastrar_clientes, name='cadastrar_clientes'),
    path('clientes/delete/<uuid:pk>', excluir_cliente, name='excluir_cliente'),
    path('clientes/alterar/<uuid:pk>', alterar_cliente, name='alterar_cliente'),

    # Produtos

    path('produtos/', produtos, name='produtos'),
    path('produtos/cadastro/', cadastrar_produtos, name='cadastrar_produtos'),

    # Venda

    path('vendas/', vendas, name='vendas'),
    path('vendas/adicionar_produto', vendas_adicionar_produto, name='adicionar_produto')
]