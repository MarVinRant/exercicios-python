# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

salario = float(input('Digite o salário do funcionário: R$ '))

if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)

print(f'O novo salário será de R$ {novo:.2f}')