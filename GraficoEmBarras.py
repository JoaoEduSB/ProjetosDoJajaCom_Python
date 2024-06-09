# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Programa que simula dados em formato de barras

import matplotlib.pyplot as plt

print("")

# Função para criar o gráfico de barras
def criar_grafico_barras(valores):
    
    # Obtém a quantidade de valores na lista
    quantidade_valores = len(valores)

    # Define a largura das barras
    largura_barra = 0.5

    # Define a posição de cada barra no eixo x
    posicoes_barras = range(1, quantidade_valores + 1)

    # Cria o gráfico de barras
    plt.bar(posicoes_barras, valores, width=largura_barra, color='blue')

    # Adiciona rótulos aos eixos
    plt.xlabel('Índice')
    plt.ylabel('Valor')

    # Adiciona título ao gráfico
    plt.title('Gráfico de Barras')

    # Exibe o gráfico
    plt.show()

# Solicita ao usuário os valores para criar o gráfico de barras

valores = []
quantidade = int(input("Quantos valores deseja inserir? "))
for i in range(1, quantidade + 1):
    valor = float(input(f"Digite o valor {i}: "))
    valores.append(valor)

# Chama a função para criar o gráfico de barras com os valores fornecidos pelo usuário
criar_grafico_barras(valores)

print("")