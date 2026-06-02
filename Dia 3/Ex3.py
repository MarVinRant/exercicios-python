# Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar.

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'\033[1;32mO número {numero} é Par.\033[m')
else:
    print(f'\033[1;31mO número {numero} é Ímpar.\033[m')