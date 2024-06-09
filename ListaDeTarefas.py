# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Projeto Lista de Tarefas

print("")

# Função para adicionar uma tarefa à lista
def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para remover uma tarefa da lista
def remover_tarefa(lista_tarefas, indice):
    if indice >= 0 and indice < len(lista_tarefas):
        tarefa_removida = lista_tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Índice inválido. Tarefa não removida.")

# Função para exibir a lista de tarefas
def exibir_tarefas(lista_tarefas):
    if lista_tarefas:
        print("Lista de Tarefas:")
        for indice, tarefa in enumerate(lista_tarefas):
            print(f"{indice + 1}. {tarefa}")
    else:
        print("Lista de tarefas vazia.")

# Lista inicial de tarefas
lista_tarefas = []

# Loop principal do aplicativo
while True:
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Sair")

    # Solicita a escolha do usuário
    escolha = input("Escolha uma opção: ")

    # Executa a ação correspondente à escolha do usuário
    if escolha == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        adicionar_tarefa(lista_tarefas, tarefa)
        
    elif escolha == "2":
        
        if lista_tarefas:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            remover_tarefa(lista_tarefas, indice)
        else:
            print("Não há tarefas para remover.")
            
    elif escolha == "3":
        exibir_tarefas(lista_tarefas)
        
    elif escolha == "4":
        print("Saindo do aplicativo...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

print("")