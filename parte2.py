
def leituraDados():
    numero_itens = int(input(""))
    numero_pares = int(input(""))
    capacidade = int(input(""))

    itens = []
    for i in range(0, numero_itens):
        itens.append(int(input("")))

    pares = []
    for i in range(0, numero_pares):
        par_1 = int(input(""))
        par_2 = int(input(""))
        pares.append([par_1, par_2])

    return numero_itens, numero_pares, capacidade, itens, pares

def parcial_idiota(vetor, numero_elementos):

    soma = 0
    for item in vetor:
        soma = soma + item

    idiota = soma / numero_elementos
    return idiota


def branch_and_bound(item, capacidade):

    if item > capacidade:
        return 0

    for p in pares:
        if

    




if __name__ == '__main__':

    global numero_itens, numero_pares, capacidade, itens, pares

    numero_itens, numero_pares, capacidade, itens, pares = leituraDados()

    result = branch_and_bound(itens[0], capacidade)

    print(result)


