def readInput():

    numero_itens = int(input(""))
    numero_pares = int(input(""))
    capacidade = int(input(""))

    itens = []
    for i in range(0, numero_itens):
        itens.append(input(""))

    pares = []
    for i in range(0, numero_pares):
        par_1 = input("")
        par_2 = input("")
        pares.append([par_1, par_2])


    return numero_itens, numero_pares, capacidade, itens, pares

# def create_matrix(numero_itens, numero_pares, capacidade, itens, pares):
#
#     values = []
#     for

if __name__ == '__main__':
    numero_itens, numero_pares, capacidade, itens, pares = readInput()