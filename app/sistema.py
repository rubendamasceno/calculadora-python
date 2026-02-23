from time import sleep
from app.operacoes import *
from app.utilidades import *
from app.arquivo import *

arq = 'historico.txt'
if not existeArquivo(arq):
    criarArquivo(arq)
cabecalho(f'{'SUA CALCULADORA EM PYTHON':^40}')
def iniciar():
    while True:
        resp = menu(['Somar', 'Subtrair', 'Multiplicar', 'Dividir','Ver histórico de contas', 'Sair'])
        if resp == 1:
            while True:
                numeros = input('Digite os números para somar separados por espaços: ')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('\033[31mERRO! Você precisa digitar ao menos um número!\033[m')
                    else:
                        resultado = soma(*lista)
                        print('-' * 40)
                        print(f'\033[32mO resultado da Soma vale: {soma(*lista)}\033[m')
                        print('-' * 40)
                        cadastrarArquivo(arq, f'Soma:{resultado}')
                        break
                except ValueError:
                    print('\033[31mERRO! Por favor, digite apenas números separados por espaços!\033[m')

        elif resp == 2:
            while True:
                numeros = input('Digite os números para subtrair separados por espaços: ')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('\033[31mERRO! Você precisa digitar ao menos um número!033[m')
                    else:
                        resultado = subtracao(*lista)
                        print('-' * 40)
                        print(f'\033[32mO resultado da Subtração vale: {subtracao(*lista)}\033[m')
                        print('-' * 40)
                        cadastrarArquivo(arq, f'Subtração:{resultado}')
                        break
                except ValueError:
                    print('\033[31mERRO! por favor, digite apenas números separados por espaços!\033[m')

        elif resp == 3:
            while True:
                numeros = input('Digite os números para multiplicar separados por espaços: ')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('\033[31mERRO! Você precisa digitar ao menos um número!\033[m')
                    else:
                        resultado = multiplicar(*lista)
                        print('-' * 40)
                        print(f'\033[32mO resultado da Multiplicação vale: {multiplicar(*lista)}\033[m')
                        print('-' * 40)
                        cadastrarArquivo(arq, f'Multiplicação:{resultado}')
                        break
                except ValueError:
                    print('\033[31mERRO! Por favor, digite apenas números separados por espaços!\033[m')

        elif resp == 4:
            while True:
                numeros = input('Digite os numeros para dividir separados por espaços:')
                try:
                    lista = [float(n) for n in numeros.split()]
                    if len(lista) == 0:
                        print('\033[31mERRO! Você precisa digitar ao menos um número!\033[m')
                    else:
                        resultado = dividir(*lista)
                        if isinstance(resultado, str):
                            print(f'{resultado}')
                        else:
                            print('-' *40)
                            print(f'\033[32mO resultado da Divisão vale: {resultado:.2}\033[m')
                            print('-' *40)
                            cadastrarArquivo(arq, f'Divisão:{resultado:.2f}')
                            break
                except ValueError:
                    print('\033[31mERRO! Por favor, digite apenas números separados por espaços!\033[m')

        elif resp == 5:
            lerArquivo(arq)

        if resp == 6:
            print('-' *25)
            print('Finalizando', end='',flush=True)
            for _ in range(3):
                sleep(0.5)
                print('.', end='',flush=True)
            print()
            print('>>> Volte sempre! <<<')
            print('-' * 25)
            break



