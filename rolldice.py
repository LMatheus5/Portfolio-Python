import random

def rolar_dado(lados):
    return random.randint(1, lados)

while True:
    print("Opções de Dados:")
    print("1. D6 (Dado de 6 lados)")
    print("2. D10 (Dado de 10 lados)")
    print("3. D20 (Dado de 20 lados)")
    print("4. D100 (Dado de 100 lados)")
    print("5. Sair")

    escolha = input("Escolha um dado (1/2/3/4) ou digite 5 para sair: ")

    if escolha == "5":
        break

    if escolha in ["1", "2", "3", "4"]:
        lados_do_dado = [6, 10, 20, 100][int(escolha) - 1]
        resultado = rolar_dado(lados_do_dado)
        print(f"Resultado do dado de {lados_do_dado} lados: {resultado}\n")
    else:
        print("Escolha inválida. Tente novamente.\n")