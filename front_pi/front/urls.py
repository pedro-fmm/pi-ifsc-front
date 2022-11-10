from django.urls import path
from .views import login, home, clientes, alterar_cliente, cadastrar_clientes, detalhes_cliente, excluir_cliente, produtos, cadastrar_produtos, error, analitico, funcionario, cadastrar_funcionario, cadastrar_faixa, cadastrar_categoria, cadastrar_genero, cadastrar_plataforma, faixas, categorias, generos, plataformas, detalhes_categoria, detalhes_faixa, detalhes_genero, detalhes_plataforma, excluir_categoria, excluir_faixa, excluir_genero, excluir_plataforma

app_name = 'front'

"""
Urls do app front.
"""

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('funcionario/', funcionario, name='funcionario'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/<uuid:pk>', detalhes_cliente, name='detalhes_cliente'),
    path('clientes/cadastro/', cadastrar_clientes, name='cadastrar_clientes'),
    path('clientes/delete/<uuid:pk>', excluir_cliente, name='excluir_cliente'),
    path('clientes/alterar/<uuid:pk>', alterar_cliente, name='alterar_cliente'),
    path('produtos/<uuid:pk>', detalhes_produto, name='detalhes_produto'),
    path('produtos/', produtos, name='produtos'),
    path('produtos/cadastro/', cadastrar_produtos, name='cadastrar_produtos'),
    path('produtos/alterar/<uuid:pk>', alterar_produto, name='alterar_produto'),
    path('produtos/delete/<uuid:pk>', excluir_produto, name='excluir_produto'),
    path('error/', error, name='erro'),
    path('analitico/', analitico, name='analitico'),
    path('funcionario/cadastro/', cadastrar_funcionario, name='cadastrar_funcionario'),
    path('plataformas/', plataformas, name='plataformas'),
    path('plataforma/<uuid:pk>', detalhes_plataforma, name='detalhes_plataforma'),
    path('plataforma/delete/<uuid:pk>', excluir_plataforma, name='excluir_plataforma'),
    path('plataforma/cadastro/', cadastrar_plataforma, name='cadastrar_plataforma'),
    path('faixas/', faixas, name='faixas'),
    path('faixa/<uuid:pk>', detalhes_faixa, name='detalhes_faixa'),
    path('faixa/delete/<uuid:pk>', excluir_faixa, name='excluir_faixa'),
    path('faixa/cadastro/', cadastrar_faixa, name='cadastrar_faixa'),
    path('generos/', generos, name='generos'),
    path('genero/<uuid:pk>', detalhes_genero, name='detalhes_genero'),
    path('genero/delete/<uuid:pk>', excluir_genero, name='excluir_genero'),
    path('genero/cadastro/', cadastrar_genero, name='cadastrar_genero'),
    path('categorias/', categorias, name='categorias'),
    path('categoria/<uuid:pk>', detalhes_categoria, name='detalhes_categoria'),
    path('categoria/delete/<uuid:pk>', excluir_categoria, name='excluir_categoria'),
    path('categoria/cadastro/', cadastrar_categoria, name='cadastrar_categoria'),
]