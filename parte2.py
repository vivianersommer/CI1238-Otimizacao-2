import numpy as np


def leituraDados():

    global numero_itens, numero_pares, capacidade, itens, pares

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


def gerar_ordem_com_pares():
    dependencias = {}
    for i, item_x in enumerate(itens):
        dependencias[str(i+1)] = []

    for par in pares:
        par_1 = par[0]
        par_2 = par[1]

        array = dependencias[str(par_2)]
        array.append(par_1)
        dependencias[str(par_2)] = array

    sequencia = []

    for i, lista in enumerate(dependencias):
        i = i + 1
        lista = dependencias[str(i)]
        if len(lista) == 0:
            if sequencia.__contains__(i):
                continue
            else:
                sequencia.append(i)
        else:
            for dependencia in lista:

                dependencia_na_lista = False
                pai_na_lista = False

                # testa se dependencia ja esta em ordem
                for pos, j in enumerate(sequencia):
                    if j == dependencia:
                        dependencia_na_lista = True
                        index_dependencia_sequencia = pos
                        break

                # testa se o "pai" ja esta na lista
                for pos, j in enumerate(sequencia):
                    if i == j:
                        pai_na_lista = True
                        index_pai_lista = pos
                        break

                # se os dois ja estiverem na lista, analisar se ordem esta certa
                if pai_na_lista and dependencia_na_lista:
                    if index_pai_lista < index_dependencia_sequencia:
                        a = sequencia[index_pai_lista]
                        sequencia[index_pai_lista] = sequencia[index_dependencia_sequencia]
                        sequencia[index_dependencia_sequencia] = a

                if not dependencia_na_lista:
                    sequencia.append(dependencia)

            if sequencia.__contains__(i):
                continue
            else:
                sequencia.append(i)

    return sequencia


def analizar_pares(item):

    item = item + 1
    ordem = gerar_ordem_com_pares()

    for i in ordem:
        if i == item:
            index = i
            break

    for j in ordem:
        if j < index:
            # se na ordem, já deveria ter ido outros itens
            # analisar se esses outros itens já foram
            if viagens[j] == 0:
                return False

    return True


def branch_and_bound(posicao, capacidade, viagem_atual):

    # IDEIA GERAL
    # testar de item cabe na viagem
    # testar de item está na lista de pares, se estiver, testar condição
    # testar de chamando parcial_idiota, o valor é menor do que o já obtido
    # se passar em todos os testes, entrar na recursão

    if posicao >= numero_itens:
        return

    item = itens[posicao]

    if viagens[posicao] != 0:
        print("Item já viajou")
        branch_and_bound(posicao + 1, capacidade, viagem_atual)

    if viagens[viagem_atual] + item <= capacidade and analizar_pares(posicao):  # testar de item está na lista de pares, se estiver, testar condição
        print("Item é viavel")
        # atualizar viagem do item e os pesos
        viagens[posicao] = viagem_atual
        pesos[posicao] = pesos[posicao] + item
        branch_and_bound(posicao + 1, capacidade, viagem_atual)

    else:
        print("Item não é viável")
        branch_and_bound(posicao - 1, capacidade, viagem_atual)

    # if parcial_idiota([],0) <= otimo: #o que passar para a parcial??
    #     branch_and_bound(item + itens[i+1], capacidade - item)


if __name__ == '__main__':

    global viagens, pesos

    numero_itens, numero_pares, capacidade, itens, pares = leituraDados()

    viagens = np.zeros(numero_itens)

    pesos = np.zeros(numero_itens)

    branch_and_bound(0, capacidade, 1)

    print(viagens)

# 5 2 10
# 5 6 4 8 5
# 2 3
# 5 1


