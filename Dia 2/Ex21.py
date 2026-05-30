# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input('Digite seu nome completo: ').strip()

# Divide o nome em uma lista
nome_fatiado = nome.split()

print(f'Fico muito feliz em te conhecer {nome}!')
print(f'Primeiro nome: {nome_fatiado[0]}')
print(f'Último nome: {nome_fatiado[-1]}')