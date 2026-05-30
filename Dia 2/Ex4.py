# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite um valor em metros: "))
# centimetros = metros * 100
# milimetros = metros * 1000

# print(f"{metros} metros equivalem a {centimetros} centímetros.")
# print(f"{metros} metros equivalem a {milimetros} milímetros.")

print(f"{metros} metros equivalem a {metros * 100} centimetros.")
print(f"{metros} metros equivalem a {metros * 1000} milimetros.")