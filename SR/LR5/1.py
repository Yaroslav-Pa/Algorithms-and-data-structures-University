from collections import defaultdict, deque
from variables1 import add_edges, start_vertex, distance_to_find
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start, distance):
        visited = set()
        result = []

        queue = deque([(start, 0)])
        
        while queue:
            current, current_distance = queue.popleft()

            if current_distance == distance:
                result.append(current)

            if current_distance < distance:
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_distance + 1))

        if start in result:
            result.remove(start)
        return result

graph = Graph()

for edge in add_edges:
    vertex1, vertex2 = edge
    graph.add_edge(vertex1,vertex2)
# for _ in range(edges):
#     u, v = map(int, input("Введіть ребро (формат: вершина1 вершина2): ").split())
#     graph.add_edge(u, v)


result_vertices = graph.bfs(start_vertex, distance_to_find)
print(f"Вершини на відстані {distance_to_find} від вершини {start_vertex}: {result_vertices}")
