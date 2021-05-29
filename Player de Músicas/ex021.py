from musicPlay import *
from tools import cor

opcoes = menuopc()

while True:
    print(cor())
    print(f'{" Player de músicas ":=^45}')

    for i, v in enumerate(opcoes):  # Imprime o menu de opções
        print(f'[ {cor(str(i), "verde", True)} ] {v if v == "Sair" else v[:-4]}')

    user = int(input('>> '))

    if user < 0:
        user *= -1

    if user < len(opcoes):
        if opcoes[user] == 'Sair':
            print(f'{cor("Finalizando...", "cinza", True)}')
            break

        else:
            playmusic(user)

    else:
        print(f'{cor("Opção Inválida!", "vermelho", True)}')
