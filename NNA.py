import sys
from graph import *
from util import  *
import random


def findNearNeighbor(edge, graph, allocated):
    nums = list(range(1, graph.size+1))
    random.shuffle(nums)
    near = random.choice(nums)
    if near in allocated:
       # print(allocated, near)
        while(near in allocated) and nums: # gera um mais proximo aleatorio
            random.shuffle(nums)
            near = nums.pop()
    else:
        for i in range(1, graph.size+1):
            if i != edge:
                if (graph.distances[edge, i] < graph.distances[edge, near]) and (near not in allocated):
                    near = i

    return near

def allAllocated(allocated, graph):
    if len(allocated) < graph.size:
        return False
    return True

def nearestNeighbor(graph):
    print("Processing...")
    solution = [] # solution
    allocated = {}

    while(not allAllocated(allocated, graph)): #se ainda precisa alocar
        route = [0]
        current = 0


        while cost(route, graph) <= graph.vehiclesCapacity: #enquanto ainda pode entregar
            last = route.copy()

            next = findNearNeighbor(current, graph, allocated)

            if(current == next):
                break

            if next not in allocated:
                current = next
                route.append(next)
                allocated[next] = True
        route = last.copy()
        route.append(0)
        solution.append(route)
    return(solution)