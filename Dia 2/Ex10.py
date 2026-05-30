# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
# Ex: Digite um numero: 6.127
# O número tem a parte inteira: 6

import math

num  = float(input("Digite um valor: "))
porcao_inteira = math.trunc(num) # trunc, que corta a parte decimal do número e deixa apenas a parte inteira.

print(f"O valor digitado foi {num} e a sua porção inteira é {porcao_inteira}.")