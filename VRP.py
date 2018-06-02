###############################################################################
#       ALGORITMO DESENVOLVIDO PARA DISCIPLINA INTELIGENCIA ARTIFICIAL        #
#   OBJETIVO: SOLUCAO EFICIENTE PARA O PROBLEMA DE ROTEAMENTO DE VEICULOS     #
#   AUTOR: GUSTAVO CARDOZO RODRIGUES    151151460         DATA:03-06-2018     #
#  UNIVERSIDADE FEDERAL DO PAMPA - CAMPUS ALEGRETE       7 PERIODO - NOITE    #
#   CONTATO :  gustavocrod@outlook.com, gustavocrod.unipampa@gmail.com        #
###############################################################################
import sys
from graph import *
from CEWS import *
from NNA import *
from util import *
from MCCEWS import *

def VRP(graph):
    graph.calcDistances()
    solution = MonteCarloSavings(graph)
    #solution = ClarcAndWright(graph)
    showResult(solution, graph)

def read():
    string = input("")
    numConsumers, vehiclesCapacity = map(int, string.split())
    graph = Graph(numConsumers, vehiclesCapacity)

    string = input("")
    warehouseX, warehouseY = map(int, string.split())

    graph.setWarehouse(warehouseX, warehouseY)

    for x in range(numConsumers):
        string = input("")
        consumX, consumY, consumDeman = map(int, string.split())
        node = Node(x+1, consumX, consumY, consumDeman)
        graph.addNode(node)

    return graph


def main():
    graph = read()
    VRP(graph)

if __name__ == "__main__":
    main()