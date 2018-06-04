from graph import *

def cost(route, graph):
    """
    Funcao que computa a soma das demandas dos clientes de uma rota
    :param route: rota a ser computada
    :param graph: grafo
    :return:
    """
    cost = 0

    for i in route:
        edge = graph.findEdge(i)
        cost += edge.demand
    return cost

def showResult(routes, graph):
    print("Result:")
    for route in routes:
        for i in route:
            print(str(i) + " ", end="")
        print()
    print("Custo total: " + str(totalCost(routes, graph)))

def totalCost(routes, graph):
    """
    Funcao q computa o somatorio das distancias de todas as rotas
    :param routes:
    :param graph:
    :return:
    """
    cost = 0
    for route in routes:
        for i in range(1, len(route)):
            cost += graph.distances[route[i-1], route[i]] # e.g: cost += graph.distances[0, 1]
    return cost

def insertWarehouse(routes):
    """
    adiciona o deposito nas rotas, inicio e fim
    :param routes:
    :return:
    """
    for route in routes:
        route.insert(0, 0) # inicio
        route.append(0) # fim

def usage():
    print("Voce deve executar o programa redirecionando um arquivo para a entrada padrao.")
    print("e.g  $ python VRP < vrpnc1.txt")

def distance(distFunction, node1, node2):
    return distFunction(node1, node2)

def euclidean(node1, node2):
    """
        sqrt( (xf - xi)^2 + (yf - yi)^2 )

    """
    if node1 == node2:
        return 0.0

    return math.sqrt(math.pow(node1.x - node2.x, 2) + math.pow(node1.y - node2.y, 2))

def absolute(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)
