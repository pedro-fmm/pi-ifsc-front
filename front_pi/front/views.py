from asyncio.log import logger
import json
import requests
from django.shortcuts import render, redirect
from toolbox import validaEmail
from front_pi.settings import API_URL
from .decorators import is_authenticated
from toolbox import validate_cpf, validate_cadastro_cliente
import logging
from uuid import uuid4
from collections import ChainMap
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

def login(request):

    if request.method == 'POST':
        email = request.POST['login-email']
        password = request.POST['login-password']
        
        if not email:
            mensagem = ['Você deve preencher o campo de e-mail']
            return render(request, 'auth/auth.html', {'messages': mensagem})
        if not validaEmail(email=email):
            mensagem = ['Você deve digitar um campo de e-mail válido']
            return render(request, 'auth/auth.html', {'messages': mensagem})
        if not password:
            mensagem = ['Você deve digitar uma senha.']
            return render(request, 'auth/auth.html', {'messages': mensagem})

        resp = requests.post(API_URL + '/api/auth/login/', {'email': email, 'password': password})
        if resp.json().get('user', False):
            request.session["Authorization"] = 'Bearer ' + resp.json().get('access')
            return render(request, 'home/home.html')
        mensagem = ['Usuário ou senha inválidos']
        return render(request, 'auth/auth.html', {'messages': mensagem})
        
    return render(request, 'auth/auth.html')

@is_authenticated
def home(request):

    vendas = requests.get(API_URL + '/api/venda/list/', headers={'Authorization': request.session['Authorization']}).json()

    logger.warn(vendas)

    return render(request, 'home/home.html', {'titulo': 'Home', 'vendas': vendas})

@is_authenticated
def clientes(request):
    resp = requests.get(API_URL + '/api/cliente/list/', headers={'Authorization': request.session['Authorization']})
    return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})

@is_authenticated
def cadastrar_clientes(request):
    if request.method == 'POST':
        nome        = request.POST['cliente-nome']
        cpf         = request.POST['cliente-cpf'].replace('.', '').replace('-', '')
        email       = request.POST['cliente-email']
        telefone    = request.POST['cliente-telefone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        endereco    = request.POST['cliente-endereco']

        validate = validate_cadastro_cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco)

        if not validate['status']:
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': validate['message']}) 

        response = requests.post(API_URL + '/api/cliente/create/', headers={"Authorization": request.session["Authorization"]}, json=validate['data'])

        if response.status_code != 201:
            mensagem = ['Falha na realização do cadastro']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem}) 
                  
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})

    return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente'})

@is_authenticated
def detalhes_cliente(request, pk):

    response = requests.get(f'{API_URL}/api/cliente/{pk}', headers={'Authorization': request.session['Authorization']})

    return render(request, 'clientes/detalhes_cliente.html', {'titulo': 'Detalhes do cliente', 'cliente': response.json()})

@is_authenticated
def excluir_cliente(request, pk):

    response = requests.delete(f'{API_URL}/api/cliente/{pk}', headers={'Authorization': request.session['Authorization']})

    if response.status_code != 204:
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/detalhes_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})
    
    mensagem = ['Cliente deletado com sucesso!']

    return render(request, 'clientes/detalhes_cliente.html', {'titulo': 'Detalhes do cliente', 'messages': mensagem})

@is_authenticated
def alterar_cliente(request, pk):


    if request.method == 'POST':
        nome        = request.POST['cliente-nome']
        cpf         = request.POST['cliente-cpf'].replace('.', '').replace('-', '')
        email       = request.POST['cliente-email']
        telefone    = request.POST['cliente-telefone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        endereco    = request.POST['cliente-endereco']

        validate = validate_cadastro_cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco)

        if not validate['status']:
            return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': validate['message']}) 

        cliente = validate['data']
        response = requests.put(f'{API_URL}/api/cliente/{pk}', headers={"Authorization": request.session["Authorization"]}, json=cliente)

        if response.status_code != 200:
            mensagem = ['Falha na realização do cadastro']
            return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem}) 
                  
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})

    
    response = requests.get(f'{API_URL}/api/cliente/{pk}', headers={'Authorization': request.session['Authorization']})

    cliente = response.json()

    return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Alterar cliente', 'cliente': cliente})

def produtos(request):
    return render(request, 'produtos/produtos.html', {'titulo': 'Produtos'})


@is_authenticated
def cadastrar_produtos(request):

    resp_plat = requests.get(API_URL + '/api/plataforma/list/', headers={'Authorization': request.session['Authorization']})
    resp_gen = requests.get(API_URL + '/api/genero/list/', headers={'Authorization': request.session['Authorization']})
    resp_faixa = requests.get(API_URL + '/api/faixa/list/', headers={'Authorization': request.session['Authorization']})        
    resp_cate = requests.get(API_URL + '/api/categoria/list/', headers={'Authorization': request.session['Authorization']})

    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        imagem = request.FILES
        plataforma = request.POST['plataformas']
        genero = request.POST['generos']
        faixa_etaria = request.POST['faixas']
        categoria = request.POST['categorias']
        estoque = request.POST['estoque']

        if not nome:
            mensagem = ['Você deve preencher o campo de nome']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not descricao:
            mensagem = ['Você deve preencher o campo de descrição']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not imagem:
            mensagem = ['Você deve preencher o campo de imagem']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not plataforma:
            mensagem = ['Você deve preencher o campo de plataforma']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not genero:
            mensagem = ['Você deve preencher o campo de gênero']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not faixa_etaria:
            mensagem = ['Você deve preencher o campo de faixa etária']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not categoria:
            mensagem = ['Você deve preencher o campo de categoria']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})
        if not estoque:
            mensagem = ['Você deve preencher o campo de estoque']
            return render(request, 'produtos/cadastrar_produtos.html', {'messages': mensagem})

        data = {
            'nome': nome,
            'descricao': descricao,
            'imagem': imagem,
            'plataforma': plataforma,
            'genero': genero,
            'faixa_etaria': faixa_etaria,
            'categoria': categoria,
            'estoque': estoque,
        }

        resp = requests.post(API_URL + '/api/produto/create/', data, headers={'Authorization': request.session['Authorization']})

        if resp.status_code == '201':
            mensagem = ['Produto adicionado com sucesso!']
            render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat.json(), 'generos': resp_gen.json(), 'faixas': resp_faixa.json(), 'categorias': resp_cate.json(), 'messages': mensagem})        
    
        render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat.json(), 'generos': resp_gen.json(), 'faixas': resp_faixa.json(), 'categorias': resp_cate.json(), 'messages': mensagem})

    return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat.json(), 'generos': resp_gen.json(), 'faixas': resp_faixa.json(), 'categorias': resp_cate.json()})

@is_authenticated
def vendas_list(request):
    vendas = requests.get(API_URL + '/api/venda/list/', headers={'Authorization': request.session['Authorization']}).json()
    return render(request, 'vendas/vendas.html', {'titulo': 'Vendas', 'vendas': vendas})

@is_authenticated
def vendas_iniciar(request):
      
    if request.session.get('produtos', None) != None:
        produtos_id = set(request.session['produtos'])
        produtos = []

        for produto_id in produtos_id:
            logger.warn(produto_id)
            produtos.append(requests.get(f'{API_URL}/api/produto/{produto_id}', headers={'Authorization': request.session['Authorization']}).json())
        logger.warn(produtos)

        return render(request, 'vendas/venda.html', {'titulo': 'Venda', 'produtos': produtos})
    return render(request, 'vendas/venda.html', {'titulo': 'Venda'})

@is_authenticated
def vendas_adicionar_produto(request):
  
    if request.method == 'POST':
        id = request.POST['produto-id']

        if request.session.get('produtos', None) != None:
            request.session['produtos'] += [f'{str(id)}']
        else: 
            request.session['produtos'] = [f'{str(id)}']
        logger.warn(request.session['produtos'])
        request.method = 'GET'
        return vendas_iniciar(request)

    resp_produto = requests.get(API_URL + '/api/produto/list/', headers={'Authorization': request.session['Authorization']})

    return render(request,  'vendas/adicionar_produto.html', {'titulo': 'Adicionar produto', 'produtos': resp_produto.json()})

@is_authenticated
def vendas_realizar(request):

    if request.method == 'POST':
        if request.session.get('produtos', None) != None:
            
            venda_data = {"cliente": '21fb9fe0-283b-442b-a30d-d07fda18dae2', "valor": "0", "vendedor": "2"}
            response_venda = requests.post(f'{API_URL}/api/venda/create/', data=venda_data, headers={'Authorization': request.session['Authorization']})
            id_venda = response_venda.json()['id']

            id_produtos = request.session.get('produtos', None)
            id_produtos_venda = []

            for produto in id_produtos:
                produto_data = {"produto": produto, "venda": id_venda}
                id_produtos_venda.append(requests.post(f'{API_URL}/api/vendaitem/create/', data=produto_data, headers={'Authorization': request.session['Authorization']}))

            request.session['produtos'] = None
            return render(request, 'vendas/venda_realizada.html', {'titulo': 'venda realizada', 'message': f'foi {id_venda}, {id_produtos_venda}'})

    return render(request, 'vendas/venda_realizada.html', {'titulo': 'venda realizada', 'message': 'nao foi'})

@is_authenticated
def vendas_get_cliente(request):
    # if request.method == 'POST':
        # venda = requests.post(f'{API_URL}/api/clientes/{uuid}', data, headers={'Authorization': request.session['Authorization']})
        # request.session.get('produtos', None)
    return None

@is_authenticated
def vendas_deletar(request, pk):
    
    response = requests.delete(f'{API_URL}/api/venda/{pk}', headers={'Authorization': request.session['Authorization']})

    if response.status_code == 204:
        mensagem = ['Venda deletada com sucesso!']
        vendas = requests.get(API_URL + '/api/venda/list/', headers={'Authorization': request.session['Authorization']}).json()
        return render(request, 'vendas/vendas.html', {'titulo': 'Vendas', 'vendas': vendas, 'messages': mensagem})

    mensagem = ['Ocorreu um erro.']
    return render(request, 'vendas/vendas.html', {'titulo': 'Vendas', 'vendas': vendas, 'messages': mensagem})
    