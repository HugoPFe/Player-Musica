from os import listdir, getcwd
from tools import titulo


def playmusic(opc):
    """
    → Reproduz a música até o usuário deixar o volume no 0.
    :param opc: Recebe o índice da música.
    :return: Sem retorno.
    """
    print('\033[37m')
    from pygame import mixer
    from pygame import init
    print('\033[m')

    init()
    mixer.init()
    titulo(f' TOCANDO: {musicas[opc]} ')
    mixer.music.load(dirmsc+musicas[opc])
    volume = 0.2
    mixer.music.play(start=mscstart[opc], fade_ms=1500)

    while volume != 0:
        mixer.music.set_volume(volume)
        volatual = mixer.music.get_volume()
        print(f'Volume atual: {volatual * 10:.0f}')
        volume = float(input('Volume (0 sai): ')) / 10

    mixer.music.stop()


def addmusic(msc: str):
    """
    → Adiciona uma música à lista "opcoes".
    :param msc: Recebe o nome do arquivo da música.
    :return: Sem retorno.
    """
    opcoes.insert(-1, msc)


def addstrt(start: float):
    """
    → Adiciona o tempo de começo de uma música (segs), à lista.
    :param start: Recebe o segundo de começo.
    :return: Sem retorno.
    """
    mscstart.append(start)


def menuopc():
    return opcoes


opcoes = ['Sair']  # Lista de opções
mscstart = list()
tempstart = [53, 24, 178.5, 24, 55, 54]
dirmsc = getcwd()+'/musicPlay/musics/'
musicas = listdir(dirmsc)

for m in musicas:
    addmusic(m)

for s in tempstart:
    addstrt(s)
