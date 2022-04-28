
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

    # IDEIA GERAL
    # testar de item cabe na viagem
    # testar de item está na lista de pares, se estiver, testar condição
    # testar de chamando parcial_idiota, o valor é menor do que o já obtido
    # se passar em todos os testes, entrar na recursão

    if item > capacidade:
        return 0

    for p in pares:
        if item == p[0]:
            # viagem a deve ir antes de b , nesse caso item é o a
            print("Testar se item b já não foi")
        if item == p[1]:
            # viagem b deve ir depois de a , nesse caso item é o b
            print("Testar se item a já foi")

    if parcial_idiota([],0) <= otimo: #o que passar para a parcial??
        branch_and_bound(item + itens[i+1], capacidade - item)





    




if __name__ == '__main__':

    global numero_itens, numero_pares, capacidade, itens, pares, otimo, i

    otimo = numero_itens

    i = 0

    numero_itens, numero_pares, capacidade, itens, pares = leituraDados()

    result = branch_and_bound(itens[0], capacidade)

    print(result)


