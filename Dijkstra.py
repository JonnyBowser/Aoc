import sys


def dijkstra(graph, start, end):
    unVisited = graph
    distances = {}
    prevNode = {}
    path = []

    for node in graph:
        distances[node] = 1000000
    distances[start] = 0

    while unVisited:
        # find the smallest total distance available
        minNode = None
        for node in unVisited:
            if minNode == None:
                minNode = node
            elif distances[node] < distances[minNode]:
                minNode = node

        # update the current distances if it's better
        options = graph[minNode].items()
        for node, distance in options:
            if distances[minNode] + distance < distances[node]:
                distances[node] = distances[minNode] + distance
                prevNode[node] = minNode

        # make sure we don't visit this node again
        unVisited.pop(minNode)

    # rewind the path that it took
    node = end
    while node != start:
        path.insert(0, node)
        node = prevNode[node]
    path.insert(0, node)

    # print the information
    print("Total distance for best path:", distances[end])
    print("Best path:", ", ".join(path))


graph = {}
# MAKE THIS EITHER DIRECTED OR UNDIRECTED
for line in sys.stdin:
    first, _, second, _, distance = line.split()  # CHANGE THIS LINE
    distance = int(distance)
    if not first in graph:
        graph[first] = {}
    if not second in graph:
        graph[second] = {}
    graph[first][second] = distance
    graph[second][first] = distance

dijkstra(graph, "London", "Belfast")  # CHANGE THIS LINE
