# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta_necessaria = area / 2

print(f"A área da parede é: {area:.2f} m²")
print(f"A quantidade de tinta necessaria para pintar a parede é: {tinta_necessaria:.2f} litros")
print("Lembre-se de comprar um pouco mais de tinta para garantir que você tenha o suficiente para cobrir toda a parede, especialmente se houver imperfeições ou se a parede for porosa.")