from graph import *
from util import *

'''
    Baseado no artigo "Capacitated vehicle routing system applying Monte Carlo methods"
    de Romulo Augusto de Carvalho Oliveira e Karina Valdivia Delgado
    may 26-29, 2015
    
    disponivel em: http://www.seer.unirio.br/index.php/isys/article/view/5163/4917
    
    Algoritmo Clarke e Wright
'''


def createInitialRoutes(graph):
    """
    Cada cliente i vai pra uma nova rota r = (0, i, 0)
    que vai do deposito ao cliente e retorna ao deposito

    :param graph:
    :return: retorn a lista com as n rotas
    """
    routes = []  # solucao
    for i in range(1, graph.size+1):
        routes.append([i] ) # nao adicionando o deposito para melhor manutencao do codigo
    return routes

def computeSavingsList(graph):
    """
    savings_list = {};
    foreach i, j ∈ V - {0} do
        Sij = C(0, i) + C(0, j) - C(i, j);
        savings_list <- Si, j;
    sort_decreasing(savings_list);
    return savings_list;

    :param graph: objeto grafo contendo as distancias e o tamanho
    :return: lista de savings, ordenada por ordem decrescente de economia
    """
    list = []
    for i in range(1, graph.size+1):
        for j in range(1, graph.size+1):
            if i != j:
                save = graph.distances[i, 0] + graph.distances[0, j] - graph.distances[i, j] # sij = di0 + d0j − dij , for all i, j ≥ 1 and i != j;
                list.append([(i, j), save])

    list.sort(key=lambda x: x[1], reverse=True)  # ordena a lista de saves, decrescente
    return list


def feasibleMerge(i, j, routes, graph):
    """
    Para duas rotas (r e s) serem factiveis de fusao,
     i deve ser o ultimo cliente a ser visitado na sua rota r
     j deve ser o primeiro cliente a ser visitado na sua rota s
     < ou ao contrario >
    e se a soma das demandas dos clientes das duas rotas nao excede a capacidade maxima

    :param i:
    :param j:
    :param routes: lista de rotas
    :param graph: grafo
    :return:
    """
    r, s = [], [] # rota inicial e final
    for route in routes: # percorre cada rota
        if route[0] == j: # se a rota começar com j
            r = route # rota inicial eh agora, a rota q iniciou com j
        elif route[-1] == i: # se a rota termina com i
            s = route # a rota final agora eh a rota q termina com i

        if r and s: # se as rotas existem, ou seja, se existiu alguma rota q comecou com j e outra q terminou com i
            if (cost(r, graph) + cost(s, graph) <= graph.vehiclesCapacity): # ele testa se o somatorio das demandas das duas rotas nao excede a capacidade maxima
                return True # se nao exceder, entao SIM. as rotas podem ser unidas

    return False

def mergeRoutes(i, j, routes):
    """
    Faz um merge entre as rotas r e s, sendo:
        r a rota que contem j: r = (0, ..., j, 0)
        s a rota que contem i: s = (0, i, ..., 0)

    :param i:
    :param j:
    :param routes:
    :return:
    """
    r, s = [], []
    for route in routes:
        if route[0] == j:
            r = route
        elif route[-1] == i:
            s = route

    routes.remove(r) # remove r
    routes.remove(s) # remove s
    routes.append(r + s)


def ClarkeAndWright(graph):
    """
    1 - routes <- create_initial_routes(V);
    2 - savings_list = compute_savings_list(V);
    3 - foreach i, j ∈ savings_list do
        4 - if feasible_merge(i, j, Q) then
            5 - routes <- merge_routes(i, j)

    o passo 5 o algoritmo tenta fundir as rotas as quais i e j pertencem
    :param graph:
    :return:
    """
    solution = (createInitialRoutes(graph)).copy() # cria rotas com as cidades apenas - passo 1
    listOfSaves = computeSavingsList(graph) # lista de economias - passo 2
    for save in listOfSaves: # passo 3
        i, j = save[0]
        if (feasibleMerge(i, j, solution, graph)):
            mergeRoutes(i, j, solution) # passo 5


    insertWarehouse(solution)
    return solution

