import re
from itertools import zip_longest


def __is_cpf_calcula_digito(cpf):
    soma = 0
    for dig, mult in zip_longest(cpf, range(len(cpf) + 1, 1, -1)):
        soma += int(dig) * mult
    resto = soma % 11

    if resto < 2:
        cpf += str(0)
    else:
        cpf += str(11 - resto)

    return cpf


def is_cpf(cpf):
    cpf_original = re.sub(r'\D', '', str(cpf))

    if len(cpf_original) != 11:
        return False

    cpf_verificado = cpf_original[:9]

    cpf_verificado = __is_cpf_calcula_digito(cpf_verificado)
    cpf_verificado = __is_cpf_calcula_digito(cpf_verificado)

    if cpf_original[9:11] == cpf_verificado[9:11]:
        return True
    else:
        return False
