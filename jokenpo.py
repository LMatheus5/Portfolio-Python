import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagens_jogo = [pedra, papel, tesoura]

jogar_novamente = True

while jogar_novamente:
    escolha_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
    print(imagens_jogo[escolha_usuario])

    escolha_computador = random.randint(0, 2)
    print("O computador escolheu:")
    print(imagens_jogo[escolha_computador])

    if escolha_usuario >= 3 or escolha_usuario < 0: 
        print("Você digitou um número inválido, você perde!") 
    elif escolha_usuario == 0 and escolha_computador == 2:
        print("Você venceu!")
    elif escolha_computador == 0 and escolha_usuario == 2:
        print("Você perdeu")
    elif escolha_computador > escolha_usuario:
        print("Você perdeu")
    elif escolha_usuario > escolha_computador:
        print("Você venceu!")
    else:
        print("É um empate")

    resposta = input("Deseja jogar novamente? Digite 'sim' para jogar novamente ou 'não' para sair: ")
    if resposta.lower() != "sim":
        jogar_novamente = False