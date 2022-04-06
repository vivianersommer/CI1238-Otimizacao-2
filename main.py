from scipy.optimize import linprog

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
    values_eq = []  # matrix
    values_un = []
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

        values_eq.append(line)
        temp += numero_itens

    # [ peso1, peso2, peso3, 0, 0, 0 , 0, ...]
    # [ 0, 0, 0, peso1, peso2, peso3, 0, 0, 0 , 0,...]
    temp = 0
    loc_peso = (numero_itens * numero_itens)
    for i in range(0, numero_itens):  # adicionar uma linha
        line = []

        for i in range(0, temp):
            line.append(0)

        it = 0
        for i in range(temp, temp + numero_itens):
            line.append(itens[it])
            it += 1

        for i in range(temp + numero_itens, (numero_itens * numero_itens) + numero_itens):
            if i == loc_peso:
                line.append( -1 * capacidade)
            else:
                line.append(0)
        loc_peso += 1

        values_un.append(line)
        temp += numero_itens

    return values_eq, values_un

def criar_funcao_otimizacao(numero_itens):
    line = []

    for i in range(0, (numero_itens * numero_itens)):
        line.append(0)

    for i in range((numero_itens * numero_itens), (numero_itens * numero_itens) + numero_itens):
        line.append(1)

    return line


def criar_limitantes_restricoes(len_A):

    b_eq = []
    b_un = []
    for i in range(0, len_A):
        b_eq.append(1)

    for i in range(0, len_A):
        b_un.append(0)

    return b_eq, b_un


def criar_limitantes_variaveis(numero_itens, numero_pares, capacidade, itens, pares):

    list = []
    for i in range(0, (numero_itens * numero_itens) + numero_itens):
        list.append((0, 1))

    return list

if __name__ == '__main__':

    # Leitura pelo teclado do Problema
    numero_itens, numero_pares, capacidade, itens, pares = leituraDados()

    # Gerar matriz com todas as restrições de capacidade e itens
    values_eq, values_un = criar_matriz_restricoes(numero_itens, capacidade, itens)

    # Gerar vetor com a função de otimização
    c = criar_funcao_otimizacao(numero_itens)

    # Gerar valores limitantes das restrições
    b_eq, b_un = criar_limitantes_restricoes(len(values_eq))

    # Todas as variáveis devem estar entre 0 e 1
    x = criar_limitantes_variaveis(numero_itens, numero_pares, capacidade, itens, pares)

    res = linprog(c, A_ub=values_un, A_eq=values_eq,
                  b_ub=b_un, b_eq=b_eq,
                  bounds=x, method="simplex")

    result = res['fun']

    print(result)

