# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também devera mostrar o tempo que falta ou que passou do prazo.


from datetime import date
nasc = int(input('Digite o ano em que nasceu: '))
atual = date.today().year
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {atual + saldo}.')
else:
    saldo = idade - 18
    print(f'Já passou {saldo} anos do tempo de alistamento.')
    print(f'Seu alistamento foi em {atual - saldo}.')