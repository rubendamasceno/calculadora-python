from app.utilidades import cabecalho

def existeArquivo(txt):
    """
    -> Verifica se um arquivo existe
    :param txt: recebe um arquivo
    :return: False or true
    """
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(txt):
    """
    -> Cria um arquivo
    :param txt: arquivo para criar
    :return: Arquivo criado
    """
    try:
        a = open(txt, 'wt+')
        a.close()
        print(f'\033[32mArquivo {txt} criado com sucesso\033[m')
    except:
        print('\03331mHouve uma pequena falha ao criar o arquivo.\033[m')

def lerArquivo(txt):
    """
    -> le um arquivo
    :param txt: arquivo para ler
    :return: lista de linhas do arquivo
    """
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
    """
    -> escreve, adiciona coisas no arquivo
    :param arq: arquivo para cadastrar
    :param conta: contas feitas no programa
    :return: histórico das contas no arquivo
    """
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












































