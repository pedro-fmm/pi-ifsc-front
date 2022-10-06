from asyncio.log import logger
import requests
from django.shortcuts import render
from .validators import validaEmail
from front_pi.settings import API_URL
from .decorators import is_authenticated
from toolbox import validate_cpf
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
    
    # try:
    #     return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})
    # except ValueError:
    #     return render(request, 'clientes/clientes.html', {'titulo': 'Clientes'}) 
    return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})

@is_authenticated
def cadastrar_clientes(request):
    if request.method == 'POST':
        nome        = request.POST['cliente-nome']
        cpf         = request.POST['cliente-cpf'].replace('.', '').replace('-', '')
        email       = request.POST['cliente-email']
        telefone    = request.POST['cliente-telefone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        cidade      = request.POST['cliente-cidade']
        endereco    = request.POST['cliente-endereco']

        if not nome:
            mensagem = ['Você deve preencher o campo de nome']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})
        if not cpf:
            mensagem = ['Você deve preencher o campo de CPF']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})
        if not validate_cpf(cpf=cpf):
            mensagem = ['Você deve cadastrar um CPF válido']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})
        if not email:
            mensagem = ['Você deve preencher o campo de e-mail']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})    
        if not validaEmail(email=email):
            mensagem = ['Você deve cadastrar um e-mail válido']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})  
        if not telefone:
            mensagem = ['Você deve preencher o campo de telefone']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})  
        if not cidade:
            mensagem = ['Você deve preencher o campo de cidade']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})  
        if not endereco:
            mensagem = ['Você deve preencher o campo de endereço']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})  

        data = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "telefone": telefone,
            "cidade": cidade,
            "endereco": endereco,
        }

        response = requests.post(API_URL + '/api/cliente/create/', headers={"Authorization": request.session["Authorization"]}, json=data)

        logger.warn(data)
        
        if response.status_code != 201:
            mensagem = ['Falha na realização do cadastro']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem}) 
                  
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})

    return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente'})

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

    logger.warn(resp_cate.json())
    logger.warn(resp_faixa.json())
    logger.warn(resp_gen.json())
    logger.warn(resp_plat.json())

    return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto', 'plataformas': resp_plat.json(), 'generos': resp_gen.json(), 'faixas': resp_faixa.json(), 'categorias': resp_cate.json()})

