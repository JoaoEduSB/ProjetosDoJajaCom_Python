# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Programa que tras a tabuada do número desejado

print("")

i = 1

# Solicita ao usuário o número para o qual deseja-se gerar a tabuada

numero = int(input("Digite um número para gerar a tabuada: "))

# Utiliza um laço de repetição for para iterar de 1 a 10 e gerar a tabuada

print(f"Tabuada do {numero}:")

for i in range(1, 11):

    resultado = numero * i

    print(f"{numero} x {i} = {resultado}")

print("")

# Este código solicita ao usuário um número para gerar a tabuada e, em seguida, utiliza um laço de repetição for para iterar de 1 a 10 e calcular o resultado da multiplicação entre o número fornecido e cada valor do intervalo. Em seguida, imprime a tabuada completa na saída padrão.