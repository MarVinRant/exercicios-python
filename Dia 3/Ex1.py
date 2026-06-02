# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

computador = randint(0, 5)
jogador = int(input('Tente adivinhar o número que pensei (de 0 até 5): '))

if jogador == computador:
    # Adicionando \033[32m no início (Verde) e \033[m no final (Limpa)
    print('\033[32mParabens você venceu!\033[m')
else:
    # Adicionando \033[31m no início (Vermelho) e \033[m no final (Limpa)
    print(f'\033[31mVocê perdeu! O número que pensei foi {computador}.\033[m')