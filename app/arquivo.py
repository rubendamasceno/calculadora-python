from app.utilidades import cabecalho

def existeArquivo(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
        print(f'\033[32mArquivo {txt} criado com sucesso\033[m')
    except:
        print('\03331mHouve uma pequena falha ao criar o arquivo.\033[m')

def lerArquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('\033[31mHouve um ERRO ao ler o arquivo!\033[m')
    else:
        cabecalho('>>> Hitórico de contas <<<')
        for linha in a:
            print(f'{linha.replace("\n", "")}')
        a.close()

def cadastrarArquivo(arq, conta):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{conta}\n')
        except:
            print('\033[31mErro ao escrever os dados.\033[m')
            a.close()












































