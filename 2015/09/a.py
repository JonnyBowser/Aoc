import sys


def loop(weight, graph, path):
    weightOptions = []
    for start in graph:
        for end in graph[start]:
            if end in graph:
                # make a copy of the graph, so I can change it
                newGraph = {i: {x: graph[i][x] for x in graph[i]} for i in graph}
                weightToAdd = newGraph[start][end]
                newGraph.pop(start)
                weightOptions += [loop(weight + weightToAdd, newGraph, path + [start])]
        node = start
    if weightOptions:
        print("MIN", min(weightOptions))
        return min(weightOptions)
    else:
        print("->".join(path + [node]), weight)
        return weight


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

loop(0, graph, [])
