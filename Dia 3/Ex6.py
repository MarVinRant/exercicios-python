# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o pirmeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceito número: '))

maior = num1
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'\033[1;32mO maior número é: {maior} \033[m')
print(f'\033[1;34mO menor número é: {menor} \033[m')









# if num1 > num2 and num1 > num3:
#     print(f'\033[1;32mO primeiro número venceu com: {num1}. \033[m')
# elif num2 > num1 and num2 > num3:
#     print(f'\033[1;32mO segundonúmero venceu com: {num2} \033[m')
# else:
#     print(f'\033[1;34mO terceio número venceu com: {num3} \033[m')