# Crie um programa que leia quanto dinheiro tem na sua carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Digite o valor em reais que você tem na carteira: R$ "))
dolares = reais / 5.25 # Valor aproximado do dólar atualmente

print(f"Com R$ {reais:.2f}, você pode comprar aproximadamente US$ {dolares:.2f} doláres.")