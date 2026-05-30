# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alu1 = input("Nome do primeiro aluno: ")
alu2 = input("Nome do segundo aluno: ")
alu3 = input("Nome do terceiro aluno: ")
alu4 = input("Nome do quarto aluno: ")

alunos = [alu1, alu2, alu3, alu4]
random.shuffle(alunos) # O shuffle embaralha a lista original

print(f"A ordem de apresentação dos alunos é: {alunos}")