def leiaInt(msg):
    """
    -> Valida números inteiros
    :param msg: recebe uma mensagem
    :return: número inteiro
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mAção interrompida pelo usuário.\033[m')
            break
            return 0
        else:
            return n

def menu(opcoes):
    for i, opcao in enumerate(opcoes):
        print(f'\033[33m{i+1}\033[m - \033[34m{opcao}\033[m')
    print('-' *20)
    opc = leiaInt('\033[35mEscolha uma opção:\033[m ')
    print('-' *20)
    return opc

def linha(msg=''):
    tam = len(msg) + 4
    print('-' * tam)

def cabecalho(msg):
    """
    -> Cria uma mensagem em cabecalho
    :param msg: recebi uma mensagem
    :return: retorna um cabeçalho
    """
    linha(msg)
    print(msg)
    linha(msg)

'''
    cores = {'limpa': '\033[m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m',
             'magenta': '\033[35m',
             'ciano': '\033[36m',
             }
'''