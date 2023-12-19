def floyd_warshall(graph):
    num_vertices = len(graph)
    vertices = list(graph.keys())

    distance_matrix = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]
    next_vertex_matrix = [[None for _ in range(num_vertices)] for _ in range(num_vertices)]

    for i in range(num_vertices):
        distance_matrix[i][i] = 0
        for neighbor, weight in graph[vertices[i]].items():
            j = vertices.index(neighbor)
            distance_matrix[i][j] = weight
            next_vertex_matrix[i][j] = j 

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
                    next_vertex_matrix[i][j] = next_vertex_matrix[i][k]

    return distance_matrix, next_vertex_matrix

def construct_path(next_vertex_matrix, start, end):
    path = []
    while start != end:
        path.append(start)
        start = next_vertex_matrix[start][end]
    path.append(end)
    return path

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

shortest_distances, next_vertex_matrix = floyd_warshall(graph)

for i in graph:
    for j in graph:
        if i != j:
            path = construct_path(next_vertex_matrix, ord(i) - ord('A'), ord(j) - ord('A'))
            path_vertices = [chr(ord('A') + vertex) for vertex in path]
            print(f"Найкоротший шлях між {i} та {j}: \n      {shortest_distances[ord(i) - ord('A')][ord(j) - ord('A')]} "
                    f"через вершини {' -> '.join(path_vertices)}")
