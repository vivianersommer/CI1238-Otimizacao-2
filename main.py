def readInput():

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

def create_matrix(numero_itens, numero_pares, capacidade, itens, pares):

    values = [] #matrix
    temp = 0
    # [ 1, 1 ,1, 0, 0 ,0 , 0,...]
    # [ 0, 0, 0, 1 ,1 ,1, 0, ...]
    for i in range(0, numero_itens): # adicionar uma linha
        line = []

        for i in range(0, temp):
            line.append(0)

        for i in range(temp, temp + numero_itens):
            line.append(1)

        for i in range(temp + numero_itens, (numero_itens * numero_itens) + numero_itens):
            line.append(0)

        values.append([line])
        temp += numero_itens

    print(values)

if __name__ == '__main__':
    numero_itens, numero_pares, capacidade, itens, pares = readInput()
    create_matrix(numero_itens, numero_pares, capacidade, itens, pares)