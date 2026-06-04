# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

# A regra matemática: a soma de dois lados deve ser sempre maior que o terceiro lado.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segmentos PODEM FORMAR um triângulo!\033[m')
else:
    print('\033[31mOs segmentos NÃO PODEM FORMAR um triângulo!\033[m')