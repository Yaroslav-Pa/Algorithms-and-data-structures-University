import heapq
import networkx as nx
import matplotlib.pyplot as plt

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

graph = {
    'A': {'B': 1, 'C': 4, 'D': 2},
    'B': {'A': 1, 'C': 2, 'D': 5, 'E': 3},
    'C': {'A': 4, 'B': 2, 'D': 1, 'E': 7},
    'D': {'A': 2, 'B': 5, 'C': 1, 'E': 6, 'F': 8},
    'E': {'B': 3, 'C': 7, 'D': 6, 'F': 1, 'G': 5},
    'F': {'D': 8, 'E': 1, 'G': 3, 'H': 9},
    'G': {'E': 5, 'F': 3, 'H': 4, 'I': 2},
    'H': {'F': 9, 'G': 4, 'I': 7, 'J': 6},
    'I': {'G': 2, 'H': 7, 'J': 5},
    'J': {'H': 6, 'I': 5}
}

start_point = 'A'
end_point = 'J'

shortest_path_length, shortest_path = dijkstra(graph, start_point, end_point)

if shortest_path_length != float('inf'):
    print(f"Найкоротший шлях між {start_point} та {end_point} дорівнює {shortest_path_length}.")
    print(f"Шлях: {shortest_path}")

    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=700, font_size=8)

    path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='g', width=2)

    edge_labels = {(i, j): graph[i][j] for i, j in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
else:
    print(f"Шлях між {start_point} та {end_point} не знайдено.")
