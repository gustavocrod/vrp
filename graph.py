import numpy as np
import math
from util import *


class Node:
    """
        Classe que representa um edge
    """
    def __init__(self, index, x, y, demand):
        self.name = index # nome do vertice
        self.x = x # coordenada x do vertice
        self.y = y # coordenada y do vertice
        self.demand = demand # demanda do vertice


class Graph:
    """
        estrutura que representa o grafo
        contem um dicionario para armazenar as distancias entre os vertices
        (possui um dicionario para as arestas)
    """
    def __init__(self, size, vehiclesCapacity):
        self.size = size #size haha
        self.vehiclesCapacity = vehiclesCapacity # capacidade dos veiculos
        self.edges = [] # lista contendo todos os vertices
        self.distances = {} # Dicionario contendo todas as distancias entre os vertices === dicionario com as arestas


    def setWarehouse(self, x, y):
        """
        adiciona o "nome" do deposito na matriz de adjacencia
        adiciona o vertice deposito a lista de vertices (edge)

        :param x: coordenada x do deposito
        :param y: coordenada y do deposito
        :return: nao retorna nada
        """
        node = Node(0, x, y, 0)
        self.edges.append(node)

    def addNode(self, node):
        """
        adiciona um vertice a lista de vertices
        :return:
        """
        self.edges.append(node)

    def calcDistances(self):
        """
        mapeia a distancia de todos os vertices com todos os vertices
        e adiciona no dicionario de distancia entre os nos
        distances[(fromNode, toNode)] = distance
        :return:
        """

        for x in range(len(self.edges)): #percorre os n nos
            for edge in self.edges: # ve edge por edge
                self.distances[(x, edge.name)] = distance(euclidean, self.edges[x], edge)

    def findEdge(self, index):
        """
        procura um vertice index pelo nome
        :param index:
        :return: o edge encontrado
        """
        for edge in self.edges:
            if index == edge.name:
                return edge
