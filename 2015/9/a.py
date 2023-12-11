import sys


def loop(graph):
    # weight should be passed in
    # somehow we need to find the minimum of all of them.
    weight = 0
    for node in graph:
        newGraph = dict(graph)
        weight += newGraph.pop(node)[node]
        if newGraph:
            loop(newGraph)


graph = {}
for line in sys.stdin:
    first, _, second, _, distance = line.split()
    distance = int(distance)
    if not first in graph:
        graph[first] = {}
    if not second in graph:
        graph[second] = {}
    graph[first][second] = distance
    graph[second][first] = distance

loop(graph)
