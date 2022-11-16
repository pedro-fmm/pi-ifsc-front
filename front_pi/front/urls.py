from django.urls import path
<<<<<<< HEAD
from .views import login, home
from .views import clientes, alterar_cliente ,cadastrar_clientes, detalhes_cliente, excluir_cliente
from .views import produtos, cadastrar_produtos, detalhes_produto, alterar_produto, excluir_produto
from .views import vendas_list, vendas_iniciar, vendas_adicionar_produto, vendas_realizar, vendas_deletar, vendas_listar_cliente, vendas_selecionar_cliente
from .views import analitico
from .views import funcionario, cadastrar_funcionario
from .views import cadastrar_faixa, cadastrar_categoria, cadastrar_genero, cadastrar_plataforma
from .views import faixas, detalhes_faixa, excluir_faixa
from .views import categorias, detalhes_categoria, excluir_categoria
from .views import generos, detalhes_genero, excluir_genero, alterar_genero
from .views import plataformas, detalhes_plataforma, excluir_plataforma
=======
from .views import auth, home, clientes, alterar_cliente, cadastrar_clientes, detalhes_cliente, excluir_cliente, produtos, cadastrar_produtos, error, analitico, funcionario, cadastrar_funcionario, cadastrar_faixa, cadastrar_categoria, cadastrar_genero, cadastrar_plataforma, faixas, categorias, generos, plataformas, detalhes_categoria, detalhes_faixa, detalhes_genero, detalhes_plataforma, excluir_categoria, excluir_faixa, excluir_genero, excluir_plataforma
from .views import detalhes_produto, alterar_produto, excluir_produto
>>>>>>> main

app_name = 'front'

"""
Urls do app front.
"""

urlpatterns = [
<<<<<<< HEAD

    path('login/', login, name='login'),
    path('home/', home, name='home'),

    # Clientes

=======
    path('login/', auth, name='login'),
    path('home/', home, name='home'),
    path('funcionario/', funcionario, name='funcionarios'),
>>>>>>> main
    path('clientes/', clientes, name='clientes'),
    path('clientes/<uuid:pk>', detalhes_cliente, name='detalhes_cliente'),
    path('clientes/cadastro/', cadastrar_clientes, name='cadastrar_clientes'),
    path('clientes/delete/<uuid:pk>', excluir_cliente, name='excluir_cliente'),
    path('clientes/alterar/<uuid:pk>', alterar_cliente, name='alterar_cliente'),
<<<<<<< HEAD

    # Produtos

    path('produtos/', produtos, name='produtos'),
    path('produtos/cadastro/', cadastrar_produtos, name='cadastrar_produtos'),
    path('produtos/<uuid:pk>', detalhes_produto, name='detalhes_produto'),
    path('produtos/alterar/<uuid:pk>', alterar_produto, name='alterar_produto'),
    path('produtos/delete/<uuid:pk>', excluir_produto, name='excluir_produto'),

    # Venda

    path('vendas/', vendas_list, name='vendas'),
    path('vendas/iniciar', vendas_iniciar, name='iniciar_venda'),
    path('vendas/realizar-venda', vendas_realizar, name='realizar_venda'), 
    path('vendas/listar-cliente', vendas_listar_cliente , name='listar_clientes_venda'),
    path('vendas/selecionar-cliente/<uuid:pk>', vendas_selecionar_cliente, name='selecionar_cliente'),
    path('vendas/deletar/<uuid:pk>', vendas_deletar, name='deletar_venda'),
    path('vendas/adicionar_produto', vendas_adicionar_produto, name='adicionar_produto'),

    # Funcionario
    
    path('funcionario/', funcionario, name='funcionario'),
    path('funcionario/cadastro/', cadastrar_funcionario, name='cadastrar_funcionario'),

    # Plataforma
    
=======
    path('produtos/<uuid:pk>', detalhes_produto, name='detalhes_produto'),
    path('produtos/', produtos, name='produtos'),
    path('produtos/cadastro/', cadastrar_produtos, name='cadastrar_produtos'),
    path('produtos/alterar/<uuid:pk>', alterar_produto, name='alterar_produto'),
    path('produtos/delete/<uuid:pk>', excluir_produto, name='excluir_produto'),
    path('error/', error, name='erro'),
    path('analitico/', analitico, name='analitico'),
    path('funcionario/cadastro/', cadastrar_funcionario, name='cadastrar_funcionario'),
>>>>>>> main
    path('plataformas/', plataformas, name='plataformas'),
    path('plataforma/<uuid:pk>', detalhes_plataforma, name='detalhes_plataforma'),
    path('plataforma/delete/<uuid:pk>', excluir_plataforma, name='excluir_plataforma'),
    path('plataforma/cadastro/', cadastrar_plataforma, name='cadastrar_plataforma'),
<<<<<<< HEAD

    # Faixas
    
=======
>>>>>>> main
    path('faixas/', faixas, name='faixas'),
    path('faixa/<uuid:pk>', detalhes_faixa, name='detalhes_faixa'),
    path('faixa/delete/<uuid:pk>', excluir_faixa, name='excluir_faixa'),
    path('faixa/cadastro/', cadastrar_faixa, name='cadastrar_faixa'),
<<<<<<< HEAD

    # Genero
    
=======
>>>>>>> main
    path('generos/', generos, name='generos'),
    path('genero/<uuid:pk>', detalhes_genero, name='detalhes_genero'),
    path('genero/delete/<uuid:pk>', excluir_genero, name='excluir_genero'),
    path('genero/cadastro/', cadastrar_genero, name='cadastrar_genero'),
<<<<<<< HEAD
    path('genero/alterar/<uuid:pk>', alterar_genero, name='alterar_genero'),
    
    # path('error/', error, name='erro'),
    path('analitico/', analitico, name='analitico'),

    # Categorias
    
=======
>>>>>>> main
    path('categorias/', categorias, name='categorias'),
    path('categoria/<uuid:pk>', detalhes_categoria, name='detalhes_categoria'),
    path('categoria/delete/<uuid:pk>', excluir_categoria, name='excluir_categoria'),
    path('categoria/cadastro/', cadastrar_categoria, name='cadastrar_categoria'),
<<<<<<< HEAD

=======
>>>>>>> main
]