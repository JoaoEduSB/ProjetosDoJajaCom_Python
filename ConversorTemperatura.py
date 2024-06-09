# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Programa que faz a conversão de temperaturas e trás os valores de 10 em 10 graus

print("")

def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcoes = ["Celsius para Fahrenheit", "Fahrenheit para Celsius"]


print("Escolha uma opção:")

for i, opcao in enumerate(opcoes, start=1):

    print(f"{i}. {opcao}")

escolha = int(input("Digite o número correspondente à opção desejada: "))

if escolha == 1:
    for celsius in range(-100, 101, 10):

        fahrenheit = celsius_para_fahrenheit(celsius)

        print(f"{celsius}°C = {fahrenheit:.1f}°F")

elif escolha == 2:
    for fahrenheit in range(-148, 213, 18):

        celsius = fahrenheit_para_celsius(fahrenheit)

        print(f"{fahrenheit}°F = {celsius:.1f}°C")

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

print("")