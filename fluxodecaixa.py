fluxo_caixa = []

print("__________________")
print("Fluxo de caixa")
print("__________________")
print("1 - Adicionar receita.")
print("2 - Adicionar despesa.")
print("3 - Ver saldo atual.")
print("\nDigite outro número para encerrar\n")

def adicionar_receita():
    nome = input("Nome: ")
    valor = float(input('Valor: '))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

def adicionar_despesa():
    nome = input("Nome: ")
    valor = float(input('Valor: '))
    fluxo_caixa.append({
        "nome": nome,
        "valor": -valor  # As despesas são valores negativos
    })

total = 0

while True:
    opcao = int(input('Digite a opção:'))

    if opcao == 1:
        adicionar_receita()
    elif opcao == 2:
        adicionar_despesa()
    elif opcao == 3:
        print("Saldo atual: R$", total)
    else:
        print("Adeus.")
        break

    total = 0
    for fc in fluxo_caixa:
        total += fc['valor']