# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)   
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minusculas é: {nome.lower()}')

# Para contar as letras sem os espaços, removemos os espaços e medimos o tamanho (len)
letras_sem_espaco = len(nome.replace(' ', ''))
print(f'Seu nome tem ao todo {letras_sem_espaco} letras (sem considerar os espaços)')

# O split() divide a string em uma lista de palavras. Pegamos o item 0 (primeiro nome) e medimos.
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras')