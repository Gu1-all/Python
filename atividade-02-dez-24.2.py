# Listas paralelas para armazenar tarefas e seus estados
tarefas = []
estados = []

def adicionar_tarefa(nome):
    tarefas.append(nome)
    estados.append("pendente")
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def marcar_como_concluida(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estados[indice] = "concluída"
        print(f"Tarefa '{nome}' marcada como concluída.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        tarefas.pop(indice)
        estados.pop(indice)
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def listar_tarefas():
    print("\nTarefas Pendentes:")
    for i, tarefa in enumerate(tarefas):
        if estados[i] == "pendente":
            print(f"- {tarefa}")
    print("\nTarefas Concluídas:")
    for i, tarefa in enumerate(tarefas):
        if estados[i] == "concluída":
            print(f"- {tarefa}")

def pesquisar_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estado = estados[indice]
        print(f"Tarefa encontrada: {nome} - Estado: {estado}")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Remover tarefa")
    print("4. Listar tarefas")
    print("5. Pesquisar tarefa")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)
    elif opcao == "2":
        nome = input("Digite o nome da tarefa a marcar como concluída: ")
        marcar_como_concluida(nome)
    elif opcao == "3":
        nome = input("Digite o nome da tarefa a remover: ")
        remover_tarefa(nome)
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        nome = input("Digite o nome da tarefa a pesquisar: ")
        pesquisar_tarefa(nome)
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")


