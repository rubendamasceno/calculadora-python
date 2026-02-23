def soma(*numeros):
    """
    -> soma os números fornecidos
    :param numeros: recebi numeros reais
    :return: a soma deles
    """
    return sum(numeros)

def subtracao(*numeros):
    """
    -> subtrai os números fornecidos
    :param numeros: recebi números reais
    :return: a subtração entre eles
    """
    res = numeros[0]
    for n in numeros[1:]:
        res -= n
    return res

def multiplicar(*numeros):
    """
    -> Multiplica os números entre si
    :param numeros: recebi números reais
    :return: a multiplicação entre eles
    """
    res = numeros[0]
    for n in numeros[1:]:
        res *= n
    return res

def dividir(*numeros):
    """
    -> Divide os números entre si e n aceita divisão por zero
    :param numeros: recebi números reais
    :return: divisão real
    """
    res = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            return "\033[31mERRO! Divisão por zero!\033[m"
        res /= n
    return res
