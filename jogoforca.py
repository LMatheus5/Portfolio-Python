# Jogo Forca

import os 

# DIGITE A PALAVRA SECRETA 
palavra_secreta = "DIGITE A PALAVRA SECRETA AQUI"
numero_tentativas = 0
letras_acertadas = ''


while True:
    
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite APENAS UMA letra.")
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada 

    palavra_digitada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_digitada += letra_secreta
        else:
           palavra_digitada += '*'

    print(palavra_digitada)

    if palavra_digitada == palavra_secreta:
        os.system("cls")
        print("Você ganhou, PARABENS!")
        print(f"A palavra secreta é: {palavra_secreta}.")
        print(f"Você precisou de {numero_tentativas} tentativas.")


        




