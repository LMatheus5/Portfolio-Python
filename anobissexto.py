ano = int(input("Digite o ano:\n"))

if ano % 4 == 0:
  if ano % 100 == 0:
    if ano % 400 == 0:
      print("Ano bissexto.")
    else:
      print("Não é um ano bissexto.")
  else:
    print("Ano bissexto.")
else:
  print("Não é um ano bissexto.")