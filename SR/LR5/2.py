from collections import defaultdict
from variables2 import add_edges
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def averageDensityF(graph):
    numVertices = 0
    numEdges = 0

    visited = defaultdict(bool)

    for node in graph.graph:
        if not visited[node]:
            counts = {'vertices': 0, 'edges': 0}
            dfs(graph.graph, node, visited, counts)
            numVertices += counts['vertices']
            numEdges += counts['edges'] // 2

    if numVertices == 0:
        return 0

    averageDensity = numEdges / numVertices
    return averageDensity

def dfs(graph, node, visited, counts):
    visited[node] = True
    counts['vertices'] += 1

    for neighbor in graph[node]:
        counts['edges'] += 1
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, counts)


g = Graph()

for edge in add_edges:
    vertex1, vertex2 = edge
    g.add_edge(vertex1,vertex2)

numVertices = len(g.graph)
numEdges = sum(len(neighbors) for neighbors in g.graph.values()) // 2

averageDensity = averageDensityF(g)

print(f"Number of vertices: {numVertices}")
print(f"Number of edges: {numEdges}")
print(f"Average density: {averageDensity}")
