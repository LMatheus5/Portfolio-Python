print("Bem vindo a calculadora de gorjeta.")
total = float(input("Qual é o valor total da conta?\n"))
porcentagem = int(input("Qual a porcentagem de gorjeta que você gostaria de dar? 10, 12 ou 15?\n"))
pessoas = int(input("A conta vai ser dividida por quantas pessoas?\n"))

valor_porcentagem = porcentagem / 100
valor_total = total * valor_porcentagem
valor_final = total + valor_total 
valor_por_pessoa = valor_final / pessoas
final = "{:.2f}".format(valor_por_pessoa)
print(f"Cada pessoa deverá pagar: R${final}.")


