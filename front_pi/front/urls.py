from django.urls import path
from .views import login, home, error
from .views import clientes, alterar_cliente ,cadastrar_clientes, detalhes_cliente, excluir_cliente
from .views import produtos, cadastrar_produtos, detalhes_produto, alterar_produto, excluir_produto
from .views import vendas_list, vendas_iniciar, vendas_adicionar_produto, vendas_realizar, vendas_get_cliente, vendas_deletar
from .views import analitico
from .views import funcionario, cadastrar_funcionario
from .views import cadastrar_faixa, cadastrar_categoria, cadastrar_genero, cadastrar_plataforma, 
from .views import faixas, detalhes_faixa, excluir_faixa
from .views import categorias, detalhes_categoria, excluir_categoria
from .views import generos, detalhes_genero, excluir_genero
from .views import plataformas, detalhes_plataforma, excluir_plataforma

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

    path('vendas/', vendas_list, name='vendas'),
    path('vendas/iniciar', vendas_iniciar, name='iniciar_venda'),
    path('vendas/realizar-venda', vendas_realizar, name='realizar_venda'), 
    path('vendas/cliente-venda', vendas_get_cliente, name='get_cliente_venda'),
    path('vendas/deletar/<uuid:pk>', vendas_deletar, name='deletar_venda'),
    path('vendas/adicionar_produto', vendas_adicionar_produto, name='adicionar_produto')
]