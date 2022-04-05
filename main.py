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


def criar_matriz_restricoes(numero_itens, capacidade, itens):
    values = []  # matrix
    temp = 0

    # [ 1, 1 ,1, 0, 0 ,0 , 0,...]
    # [ 0, 0, 0, 1 ,1 ,1, 0, ...]
    for i in range(0, numero_itens):  # adicionar uma linha
        line = []

        for i in range(0, temp):
            line.append(0)

        for i in range(temp, temp + numero_itens):
            line.append(1)

        for i in range(temp + numero_itens, (numero_itens * numero_itens) + numero_itens):
            line.append(0)

        values.append([line])
        temp += numero_itens

    # [ peso1, peso2, peso3, 0, 0, 0 , 0, ...]
    # [ 0, 0, 0, peso1, peso2, peso3, 0, 0, 0 , 0,...]
    temp = 0
    for i in range(0, numero_itens):  # adicionar uma linha
        line = []

        for i in range(0, temp):
            line.append(0)

        it = 0
        for i in range(temp, temp + numero_itens):
            line.append(itens[it])
            it += 1

        for i in range(temp + numero_itens, (numero_itens * numero_itens) + numero_itens):
            if i < (numero_itens * numero_itens):
                line.append(0)
            else:
                line.append(-1 * (capacidade))

        values.append([line])
        temp += numero_itens

    return values

def criar_funcao_otimizacao(numero_itens, numero_pares, capacidade, itens, pares):
    print("Não feito")

if __name__ == '__main__':

    # Leitura pelo teclado do Problema
    numero_itens, numero_pares, capacidade, itens, pares = leituraDados()

    # Gerar matriz com todas as restrições de capacidade e itens
    matriz_restricoes = criar_matriz_restricoes(numero_itens, capacidade, itens)

    # Gerar vetor com a função de otimização
    funcao_otimizacao = criar_funcao_otimizacao(numero_itens, numero_pares, capacidade, itens, pares)
