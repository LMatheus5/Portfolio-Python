# Calculo IMC

nome = input("Qual é o seu nome?\n")
altura = float(input("Qual é a sua altura em metros?\n"))
peso = float(input("Qual o seu peso em kg?\n"))
imc = peso / altura ** 2
print(nome, " tem", altura, " de altura")
print("pesando", peso, " quilos")
print("Seu IMC é:", imc)