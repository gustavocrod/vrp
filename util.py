from graph import *

def cost(route, graph):
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
    cost = 0
    for route in routes:
        for i in range(1, len(route)):
            #print(route[i-1], route[i])
            cost += graph.distances[route[i-1], route[i]]
    return cost


def usage():
    print("Voce deve executar o programa redirecionando um arquivo para a entrada padrao.")
    print("e.g  $ VRP < vrpnc1.txt")

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
