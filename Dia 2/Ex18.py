# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).strip()

# O método upper() converte a string para maiúsculas, facilitando a comparação
comeca_com_santo = cidade[:5].upper() == 'SANTO'

print(f'A cidade começa com "SANTO"? {comeca_com_santo}')
