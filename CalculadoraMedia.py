print("")

num_notas = int(input("Quantas notas deseja inserir? "))

soma = 0

for i in range (num_notas):
    nota = float(input(f"Digite a Nota {i+1}: "))
    soma += nota

media = soma / num_notas

print(f"A média das {num_notas} notas é: {media:.2f}")