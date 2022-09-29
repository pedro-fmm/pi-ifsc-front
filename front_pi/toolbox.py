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
