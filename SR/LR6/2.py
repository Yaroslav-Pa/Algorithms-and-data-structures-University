import heapq
import networkx as nx
import matplotlib.pyplot as plt
from variables2 import graph, start_point, end_point
def dijkstra(graph, start, end):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current, path) = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == end:
            return cost, path

        for neighbor, weight in graph[current].items():
            heapq.heappush(heap, (cost + weight, neighbor, path))

    return float('inf'), []

shortest_path_length, shortest_path = dijkstra(graph, start_point, end_point)

if shortest_path_length != float('inf'):
    print(f"Найкоротший шлях між {start_point} та {end_point} дорівнює {shortest_path_length}.")
    print(f"Шлях: {shortest_path}")

    G = nx.Graph(graph)
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=700, font_size=8)

    path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='g', width=2)

    edge_labels = {(i, j): graph[i][j] for i, j in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
else:
    print(f"Шлях між {start_point} та {end_point} не знайдено.")

plt.show()