from asyncio.log import logger
from email.mime import image
import requests
from django.shortcuts import render
from toolbox import validaEmail
from front_pi.settings import API_URL
from .decorators import is_authenticated
from toolbox import validate_cpf, validate_cadastro_cliente
import logging

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
    return render(request, 'home/home.html', {'titulo': 'Home'})

def error(request):
    return render(request, 'error/error.html', {'titulo': 'Error'})

@is_authenticated
def clientes(request):
    resp = requests.get(API_URL + '/api/cliente/list/', headers={'Authorization': request.session['Authorization']})
    try:
        return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})
    except ValueError:
        return render(request, 'error/error.html', {'titulo': 'Erro'}) 
    # return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})

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

    logger.warn(cliente)
    return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Alterar cliente', 'cliente': cliente})

def produtos(request):
    # return render(request, 'produtos/produtos.html', {'titulo': 'Produtos'})
    resp = requests.get(API_URL + '/api/produto/list/', headers={'Authorization': request.session['Authorization']})
    try:
        return render(request, 'produtos/produtos.html', {'titulo': 'Produto', 'produtos': resp.json()})
    except ValueError:
        return render(request, 'error/error.html', {'titulo': 'Erro'}) 

@is_authenticated
def excluir_produto(request, pk):

    response = requests.delete(f'{API_URL}/api/produto/{pk}', headers={'Authorization': request.session['Authorization']})

    if response.status_code != 204:
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'produto/detalhes_produto.html', {'titulo': 'Cadastro de produto', 'messages': mensagem})
    
    mensagem = ['Produto deletado com sucesso!']

    return render(request, 'produtos/detalhes_produto.html', {'titulo': 'Detalhes do produto', 'messages': mensagem})

@is_authenticated
def alterar_produto(request, pk):
    resp = requests.get(API_URL + '/api/dados/cadastro_produto/', headers={'Authorization': request.session['Authorization']})
    resp = resp.json()

    resp_gen = resp['generos']
    resp_cate = resp['categorias']
    resp_plat = resp['plataformas']
    resp_faixa = resp['faixas']

    if request.method == 'POST':
        nome = request.POST.get('produto', False)
        descricao = request.POST.get('descricao', False)
        imagem = request.FILES
        plataforma = request.POST.get('plataformas', False)
        genero = request.POST.get('generos', False)
        faixa_etaria = request.POST.get('faixas', False)
        categoria = request.POST.get('categorias', False)
        estoque = request.POST.get('estoque', False)
        preco_custo = request.POST.get('preco_custo', False)
        preco_venda = request.POST.get('preco_venda', False)

        if not nome:
            mensagem = ['Você deve preencher o campo de nome do produto']
            return render(request, 'produtos/.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not descricao:
            mensagem = ['Você deve preencher o campo de descrição']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not imagem:
            mensagem = ['Você deve preencher o campo de imagem']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not plataforma:
            mensagem = ['Você deve preencher o campo de plataforma']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not genero:
            mensagem = ['Você deve preencher o campo de gênero']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not faixa_etaria:
            mensagem = ['Você deve preencher o campo de faixa etária']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not categoria:
            mensagem = ['Você deve preencher o campo de categoria']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not estoque:
            mensagem = ['Você deve preencher o campo de estoque']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not preco_custo:
            mensagem = ['Você deve preencher o campo de preço de custo']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not preco_venda:
            mensagem = ['Você deve preencher o campo de preço de venda']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})

        data = {
            'nome': nome,
            'descricao': descricao,
            'plataforma': plataforma,
            'genero': genero,
            'faixa_etaria': faixa_etaria,
            'categoria': categoria,
            'estoque': estoque,
        }

        resp = requests.put(API_URL + '/api/produto/create/', data, files=imagem, headers={'Authorization': request.session['Authorization']})
        produto = resp.json()['id']
        data = {
            'produto': produto,
            'preco_custo': preco_custo,
            'preco_venda': preco_venda,
            'descricao': 'Primeiro preço'
        }

        resp_preco = requests.put(API_URL + '/api/preco/create/' + resp.json()['id'], data, headers={'Authorization': request.session['Authorization']})

        response = requests.get(f'{API_URL}/api/produto/{pk}', headers={'Authorization': request.session['Authorization']})

        if response.status_code != 200 and resp_preco.status_code != 201:
            mensagem = ['Falha na realização da alteração']
            return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
                  
        mensagem = ['Alteração realizada com sucesso']
        return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})

    response = requests.get(f'{API_URL}/api/produto/{pk}', headers={'Authorization': request.session['Authorization']})

    produto = response.json()

    return render(request, 'produtos/alterar_produto.html', {'titulo': 'Alteracao de Produto', 'produto': produto, 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate})

@is_authenticated
def cadastrar_produtos(request):
    resp = requests.get(API_URL + '/api/dados/cadastro_produto/', headers={'Authorization': request.session['Authorization']})
    resp = resp.json()

    resp_gen = resp['generos']
    resp_cate = resp['categorias']
    resp_plat = resp['plataformas']
    resp_faixa = resp['faixas']

    if request.method == 'POST':
        nome = request.POST.get('produto', False)
        descricao = request.POST.get('descricao', False)
        imagem = request.FILES
        plataforma = request.POST.get('plataformas', False)
        genero = request.POST.get('generos', False)
        faixa_etaria = request.POST.get('faixas', False)
        categoria = request.POST.get('categorias', False)
        estoque = request.POST.get('estoque', False)
        preco_custo = request.POST.get('preco_custo', False)
        preco_venda = request.POST.get('preco_venda', False)

        if not nome:
            mensagem = ['Você deve preencher o campo de nome do produto']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not descricao:
            mensagem = ['Você deve preencher o campo de descrição']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not imagem:
            mensagem = ['Você deve preencher o campo de imagem']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not plataforma:
            mensagem = ['Você deve preencher o campo de plataforma']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not genero:
            mensagem = ['Você deve preencher o campo de gênero']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not faixa_etaria:
            mensagem = ['Você deve preencher o campo de faixa etária']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not categoria:
            mensagem = ['Você deve preencher o campo de categoria']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not estoque:
            mensagem = ['Você deve preencher o campo de estoque']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not preco_custo:
            mensagem = ['Você deve preencher o campo de preço de custo']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
        if not preco_venda:
            mensagem = ['Você deve preencher o campo de preço de venda']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})

        data = {
            'nome': nome,
            'descricao': descricao,
            'plataforma': plataforma,
            'genero': genero,
            'faixa_etaria': faixa_etaria,
            'categoria': categoria,
            'estoque': estoque,
        }

        resp = requests.post(API_URL + '/api/produto/create/', data, files=imagem, headers={'Authorization': request.session['Authorization']})
        produto = resp.json()['id']
        data = {
            'produto': produto,
            'preco_custo': preco_custo,
            'preco_venda': preco_venda,
            'descricao': 'Primeiro preço'
        }

        resp_preco = requests.post(API_URL + '/api/preco/create/' + resp.json()['id'], data, headers={'Authorization': request.session['Authorization']})

        if resp.status_code != 201 and resp_preco.status_code != 201:
            mensagem = ['Houve um erro no servidor!']
            return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})
            
        mensagem = ['Produto adicionado com sucesso!']
        return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate, 'messages': mensagem})        
    
    return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat, 'generos': resp_gen, 'faixas': resp_faixa, 'categorias': resp_cate})

@is_authenticated
def detalhes_produto(request, pk):

    response = requests.get(f'{API_URL}/api/produto/{pk}', headers={'Authorization': request.session['Authorization']})

    return render(request, 'produtos/detalhes_produto.html', {'titulo': 'Detalhes do Produto', 'produto': response.json()})
  
@is_authenticated
def analitico(request):
    return render(request, 'analitico/analitico.html', {'titulo': 'Analítico'})

@is_authenticated
def funcionario(request):
    resp = requests.get(API_URL + '/api/funcionario/list/', headers={'Authorization': request.session['Authorization']})
    logger.warn(resp.json())
    try:
        return render(request, 'funcionario/funcionario.html', {'titulo': 'Funcionario', 'funcionarios': resp.json()})
    except ValueError:
        return render(request, 'error/error.html', {'titulo': 'Erro'}) 
    # return render(request, 'funcionario/funcionario.html', {'titulo': 'Funcionario', 'funcionario': resp.json()})

@is_authenticated
def cadastrar_funcionario(request):
    # resp = requests.get(API_URL + '/api/dados/cadastro_funcionario/', headers={'Authorization': request.session['Authorization']})
    # resp = resp.json()

    if request.method == 'POST':
        primeiroNome = request.POST['primeiro-nome']
        ultimoNome = request.POST['ultimo-nome']
        username = request.POST['username']
        comissao = request.POST['comissao']
        email = request.POST['email']
        senha = request.POST['password']
        confirmarSenha = request.POST['confirm-password']
        mensagem = 'deu pau'

        if not primeiroNome:
            mensagem = ['Você deve preencher o campo de Primeiro Nome']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if not ultimoNome:
            mensagem = ['Você deve preencher o campo de Último Nome']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if not username:
            mensagem = ['Você deve preencher o campo de Username']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if not comissao:
            mensagem = ['Você deve preencher o campo de comissao']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if not email:
            mensagem = ['Você deve preencher o campo de Email']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if not senha:
            mensagem = ['Você deve preencher o campo de Senha']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if not confirmarSenha:
            mensagem = ['Você deve preencher o campo de Confirmar Senha']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})
        if confirmarSenha != senha:
            mensagem = ['Senha não corresponde']
            return render(request, 'funcionario/cadastrar_funcionario.html', {'messages': mensagem})

        data = {
            'primeiro_nome': primeiroNome,
            'ultimo_nome': ultimoNome,
            'username': username,
            'comissao': comissao,
            'email': email,
            'password': senha
        }

        resp = requests.post(API_URL + '/api/funcionario/create/', data, headers={'Authorization': request.session['Authorization']})
        if resp.status_code == '201':
            mensagem = ['Funcionário adicionado com sucesso!']
            render(request, 'funcionario/cadastrar_funcionario.html', {'titulo': 'Cadastro de Funcionario', 'messages': mensagem})        
        
        render(request, 'funcionario/cadastrar_funcionario.html', {'titulo': 'Cadastro de Funcionario', 'messages': mensagem})

    return render(request, 'funcionario/cadastrar_funcionario.html', {'titulo': 'Cadastro de Funcionario'})
