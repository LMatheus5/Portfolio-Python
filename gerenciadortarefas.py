tarefas = []

def mostrar_menu():
    print("""
Bem-vindo ao Gerenciador de Tarefas Python
Escolha uma opção (digite apenas o número):
1 - Inserir e adicionar uma Tarefa à lista.
2 - Visualizar as Tarefas da lista.
3 - Escolher e atualizar uma Tarefa.
4 - Escolher e excluir uma Tarefa.
5 - Encerrar o programa.
    """)

def adicionar_tarefa():
    tarefa = input("Digite a Tarefa que deseja adicionar à lista: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")

def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa pendente.")
    else:
        print("Tarefas pendentes:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def atualizar_tarefa():
    visualizar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa pendente para atualizar.")
    else:
        indice = int(input("Digite o número da tarefa que deseja atualizar: "))
        if 1 <= indice <= len(tarefas):
            nova_tarefa = input("Digite a nova descrição da tarefa: ")
            tarefas[indice - 1] = nova_tarefa
            print("Tarefa atualizada com sucesso.")
        else:
            print("Número de tarefa inválido.")

def excluir_tarefa():
    visualizar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa pendente para excluir.")
    else:
        indice = int(input("Digite o número da tarefa que deseja excluir: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso.")

mostrar_menu()

while True:
    escolha = input("Escolha: ")
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        visualizar_tarefas()
    elif escolha == "3":
        atualizar_tarefa()
    elif escolha == "4":
        excluir_tarefa()
    elif escolha == "5":
        print("Obrigado por usar o Gerenciador de Tarefas. Adeus!")
        break
    else:
        print("Opção inválida. Tente novamente.")