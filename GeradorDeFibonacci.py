# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Programa que gera uma sequeência de fibonacci da quantidade de posições desejada

print("")

def fibonacci(n):
    fibonacci_seq = [0, 1]
    
    for i in range(2, n):
        proximo_numero = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]

        fibonacci_seq.append(proximo_numero)

    return fibonacci_seq

N = int(input("Digite o número de termos da sequência Fibonacci desejados: "))

sequencia_fibonacci = fibonacci(N)

print(f"Os primeiros {N} números da sequência Fibonacci são:")

for numero in sequencia_fibonacci:

    print(numero, end=" ")

print("")