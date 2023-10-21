print("Obrigado por escolher a Pizzaria Python!")
tamanho = input("Qual tamanho de pizza você deseja? P, M ou G?\n")
adicionar_pepperoni = input("Deseja adicionar pepperoni? S ou N?\n")
extra_queijo = input("Deseja mais queijo? S ou N?\n")


conta = 0
if tamanho == "P":
  conta += 15
elif tamanho == "M":
  conta += 20
else:
  conta += 25

if adicionar_pepperoni == "S":
  if tamanho == "P":
    conta += 2
  else:
    conta += 3

if extra_queijo == "S":
  conta += 1

print(f"O valor final da sua conta é: R${conta}.")