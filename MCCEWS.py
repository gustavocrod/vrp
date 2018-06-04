from graph import *
from util import *
from CEWS import *
import random

'''
    Baseado no artigo "Capacitated vehicle routing system applying Monte Carlo methods"
    de Romulo Augusto de Carvalho Oliveira e Karina Valdivia Delgado
    may 26-29, 2015
    
    disponivel em: http://www.seer.unirio.br/index.php/isys/article/view/5163/4917
    Algoritmo Monte Carlo baseado no algoritmo de Clarke e Wright
'''


def computeMCSavingsList(graph, lbda):
    """
    savings_list = {};
    foreach i, j ∈ V - {0} do
        S = C(0, i) + C(0, j) - C(i, j);
        p = random(-$, +$)
        Sij = s + (s * p)
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
                save = graph.distances[0, i] + graph.distances[0, j] - graph.distances[i, j] # sij = di0 + d0j − dij , for all i, j ≥ 1 and i != j;
                p = random.uniform(-lbda, lbda)
                save = save + (save * p)
                list.append([(i, j), save])
    list.sort(key=lambda x: x[1], reverse=True)  # ordena a lista de saves, decrescente
    return list

def MonteCarloSavings(graph):
    print("Computing...")
    best = createInitialRoutes(graph)
    insertWarehouse(best)
    for i in range(2000):
        solution = createInitialRoutes(graph)
        savingList = computeMCSavingsList(graph, 0.05)
        for save in savingList:
            i, j = save[0]
            if(feasibleMerge(i, j, solution, graph)):
                mergeRoutes(i, j, solution)

        insertWarehouse(solution)
        if totalCost(solution, graph) < totalCost(best, graph):
            best = solution
    return(best)
