# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

from datetime import date

ano = int(input('Digite um ano: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;32mO ano {ano} é bissexto.\033[m')
else:
    print(f'\033[1;31mO ano {ano} não é bissexto.\033[m')