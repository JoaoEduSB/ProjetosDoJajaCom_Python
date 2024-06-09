# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Programa que calcula a média das notas de um aluno

print("")

num_notas = int(input("Quantas notas deseja inserir? "))

soma = 0

for i in range (num_notas):
    nota = float(input(f"Digite a Nota {i+1}: "))
    soma += nota

media = soma / num_notas

print(f"A média das {num_notas} notas é: {media:.2f}")

print("")