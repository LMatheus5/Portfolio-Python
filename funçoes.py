numero_recebido = int(input("Digite um número: "))

def duplicar_num(numero):
    return numero * 2

def triplicar_num(numero):
    return numero * 3

def quadruplicar_num(numero):
    return numero * 4

resultado_duplicado = duplicar_num(numero_recebido)
resultado_triplicado = triplicar_num(numero_recebido)
resultado_quadruplicado = quadruplicar_num(numero_recebido)

print(f"Duplicado: {resultado_duplicado}")
print(f"Triplicado: {resultado_triplicado}")
print(f"Quadruplicado: {resultado_quadruplicado}")
