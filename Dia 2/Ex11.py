# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

Ca_oposto = float(input("Digite o comprimento do cateto oposto: "))
Ca_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(Ca_oposto, Ca_adjacente)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")