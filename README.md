<h1 align="center">
     🏪 Moon Store
</h1>

<h3 align="center">
    O seu comércio de jogos fácil, ágil e acessível.
</h3>

<h4 align="center">
	   Concluído🚀 
</h4>

<h2>Tabela de conteúdos</h2>

<!--ts-->

* [Sobre o projeto](#sobre)
* [Features](#features)
* [Deploy](#deploy)
* [Pré-requisitos](#requirements)
* [Como executar o projeto](#executar)
  * [Rodando a aplicação](#executar-rodas)
* [Databases](#databases)
* [Contribuidores](#contribuintes)
* [Licença](#user-content--licença)

<!--te-->

<h2 id="sobre"> 💻 Sobre o projeto </h2>

A Moon Store é um projeto desenvolvido para o Projeto Integrador do Curso Técnico Integrado do Instituto Federal de Santa Catarina

<h2 id="features"> ⚙️ Features </h2>

- [X] Users:

- Cadastro de funcionário
- Cadastro de admin

- [X] Cadastro de produtos
- [X] Cadastro de clientes
- [X] Cadastro de venda
- [X] Responsividade

<h2 id="deploy"> 🌎 Deploy </h2>

O deploy foi realizado em um Cluster Kubernetes na AWS (EKS), com uma esteira de integração contínua (CI) para o DockerHub, com entrega contínua com o FluxCD.

<h2 id="requirements"> 🛠 Pré-requisitos </h2>

As seguintes ferramentas e tecnologias foram usadas na construção do projeto:

```bash
-Python 3.10  
-Django  
-MySQL  
-Web Browser HTML5, compativel  
-Editor de códigos, como o VScode  
-Repositorio git em github.com
-Bibliotecas e demais tecnologias estão listadas 
em requirements.txt
```

<h2 id="executar"> 🚀 Como executar o projeto </h2>

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python ](https://www.python.org/)3.10.
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

O projeto, enquanto em andamento, está dentro do ambiente virtual com todas as dependências instaladas, então rodar o servidor é muito mais rápido.

<h2 id="executar-rodar">🎲 Rodando a aplicação </h2>

```bash
# Clone este repositório
git clone https://github.com/pedro-fmm/pi-ifsc-front.git

# Acesse a pasta do projeto no terminal/cmd
cd pi-ifsc-front

# Instale os requirements
pip install -r requirements.txt

# Execute a aplicação em modo de desenvolvimento
python manage.py runserver

# O servidor inciará na porta:8080 - acesse
 http://localhost:8000 
```

<h2 id="contribuintes"> 👨‍💻 Contribuidores </h2>

<table>
  <tr>
  <!-- Farias -->
    <td align="center"><a href="https://github.com/FarinhaProgrammer"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/77069076?v=4" width="100px;" alt=""/><br /><sub><b>Lucas de Farias <br>Teixeira</b></sub></a><br /></td>
    <!-- Menezes -->
    <td align="center"><a href="https://github.com/pedro-fmm"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/85511521?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Felipe<br>Matos Menezes</b></sub></a><br /></td>
    <!-- Volpato -->
    <td align="center"><a href="https://github.com/PedroLuscao"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/89154708?" width="100px;" alt=""/><br /><sub><b>Pedro Lucas<br>Volpato da Rosa</b></sub></a><br /></td>
    <!-- Cauê -->
    <td align="center"><a href="https://github.com/Caue-Lourenzo-Batista"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/102556908?v=4" width="100px;" alt="Cauê"/><br /><sub><b>Cauê Lourenzo Batista</b></sub></a><br /></td>
  </tr>
</table>

<h2 id="license">Licença</h2>

Este projeto está disponível na licença:

 GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. [https://fsf.org/](https://fsf.org/)
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

Leia mais em https://github.com/Machado-tec/readme/blob/main/LICENSE
