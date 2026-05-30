# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()

# O operador 'in' retorna True ou False
tem_silva = 'SILVA' in nome.upper().split()

print('Seu nome tem Silva? {}'.format(tem_silva))