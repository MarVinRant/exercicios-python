# Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar.

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é Par.')
else:
    print(f'O número {numero} é Ímpar.')