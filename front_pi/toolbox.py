import re

def validaEmail(email):
    regra_email = re.compile(r'^[\w-]+@[\w-]+\.[\w-]')
    if regra_email.match(email):
        return True
    return False

def validate_cnpj(cnpj: str):
    multipliers1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multipliers2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum1 = 0
    sum2 = 0

    for i in range(len(cnpj[:12])):
        sum1 += int(cnpj[i]) * multipliers1[i]

    for i in range(len(cnpj[:13])):
        sum2 += int(cnpj[i]) * multipliers2[i]

    result1 = sum1 % 11
    result2 = sum2 % 11

    if int(cnpj[12]) == (11 - result1 if result1 >= 2 else 0) and int(cnpj[13]) == (11 - result2 if result2 >= 2 else 0):
        return True

    return False


def validate_cpf(cpf: str):
    cont = 10
    sum1 = 0
    sum2 = 0

    if cpf == cpf[::-1]:
        return False

    for d in cpf[:9]:
        sum1 += int(d) * cont
        cont -= 1

    cont = 11

    for d in cpf[:10]:
        sum2 += int(d) * cont
        cont -= 1

    result1 = sum1 * 10 % 11
    result2 = sum2 * 10 % 11

    if int(cpf[9]) == (result1 if result1 < 10 else 0) and int(cpf[10]) == (result2 if result2 < 10 else 0):
        return True

    return False

def validate_cadastro_cliente(nome, cpf, email, telefone, endereco):
    if not nome:
        mensagem = ['Você deve preencher o campo de nome']
        return {'status': False, 'message': mensagem}
    if not cpf:
        mensagem = ['Você deve preencher o campo de CPF']
        return {'status': False, 'message': mensagem}
    if not validate_cpf(cpf=cpf):
        mensagem = ['Você deve cadastrar um CPF válido']
        return {'status': False, 'message': mensagem}
    if not email:
        mensagem = ['Você deve preencher o campo de e-mail']
        return {'status': False, 'message': mensagem}    
    if not validaEmail(email=email):
        mensagem = ['Você deve cadastrar um e-mail válido']
        return {'status': False, 'message': mensagem}  
    if not telefone:
        mensagem = ['Você deve preencher o campo de telefone']
        return {'status': False, 'message': mensagem}  
    if not endereco:
        mensagem = ['Você deve preencher o campo de endereço']
        return {'status': False, 'message': mensagem}

    data = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "telefone": telefone,
            "endereco": endereco,
        }

    return {'status': True, 'data': data}