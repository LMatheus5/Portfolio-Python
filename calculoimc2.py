peso = int(input("Digite seu peso:\n"))
altura = float(input("Digite sua altura em metros:\n"))
imc = peso / (altura * altura)
if imc < 18.5:
  print(f"Seu IMC é {imc}, você está abaixo do peso.")
elif imc < 25:
  print(f"Seu IMC é {imc}, você está no peso normal.")
elif imc < 30:
  print(f"Seu IMC é {imc}, você está um pouco acima do peso.")
elif imc < 35:
  print(f"Seu IMC é {imc}, você está obeso.")