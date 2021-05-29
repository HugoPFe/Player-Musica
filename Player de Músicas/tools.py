def cor(palavra: str = '', nomecor: str = 'branco', destacar: bool = False) -> str:
    """
    → Colore palavras, para destaque, ou colore o código.
    :param palavra: Recebe uma string contendo a palavra;
    :param nomecor: Recebe o joga da cor;
    :param destacar: Recebe um valor boolean, que decide se irá retornar
     apenas uma cor ou destacar uma palavra ou frase com uma cor;
    :return: Se o parâmetro DESTACAR for verdadeiro, retorna a palavra ou frase fornecida
    com a cor de preferência, se for falso, apenas retorna uma cor.

    Cores dísponiveis:
        •branco;
        •vermelho;
        •verde;
        •amarelo;
        •azul;
        •ciano;
        •cinza;
        •limpo;
        •preto.
    """
    cores = {'branco': '\033[97m', 'vermelho': '\033[91m', 'verde': '\033[92m', 'amarelo': '\033[93m',
             'azul': '\033[94m', 'limpo': '\033[m', 'ciano': '\033[96m', 'cinza': '\033[37m', 'preto': '\033[30m'}

    try:
        if destacar:
            return f'{cores[nomecor]}{palavra}{cores["branco"]}'

        else:
            return f'{cores[nomecor]}'
    except KeyError:
        print(cor(nomecor='vermelho') + 'A cor expecíficada não está disponível!' + cor())


def lin(num: int = 20, linha: str = '-=') -> None:
    print(linha * num)


def titulo(msg: str, espaços: int = 0, linha: str = '=') -> None:
    if espaços == 0:
        lenmsg = len(msg)
    else:
        lenmsg = espaços

    print(cor(), end='')
    lin(lenmsg, linha)
    print(cor(f'{msg.center(lenmsg)}', 'verde', True))
    lin(lenmsg, linha)


def leiaDinheiro(msg: str = '') -> float:
    """
    Atua como input, lendo um número (float) até o usuário digitar um número válido.
    :param msg: Recebe uma mensagem (opcional).
    :return: Um número float.
    """

    from tools import cor

    while True:
        val = input(cor() + msg).strip()

        if val.isnumeric():
            return float(val)
        else:
            if ',' in val:
                val = str(val).replace(',', '.')
                return float(val)

            elif '.' in val:
                return float(val)

            else:
                erro_msg = f'ERRO! "{val}" não é um número válido!'
                print(cor(erro_msg, "vermelho", True))


def leiaInt(msg: str = '') -> int:
    """
    Lê um número inteiro do teclado, se ocorrer uma exceção o programa pede pro usuário digitar
    um número inteiro válido.
    :param msg: Mensagem de input.
    :return: Um número inteiro lido pelo teclado.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cor(nomecor="vermelho")}Erro! Por favor digite um número INTEIRO válido!{cor()}')
        else:
            return n
