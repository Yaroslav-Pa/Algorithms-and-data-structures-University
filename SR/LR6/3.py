from variables3 import graph

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

shortest_distances, next_vertex_matrix = floyd_warshall(graph)

for i in graph:
    for j in graph:
        if i != j:
            path = construct_path(next_vertex_matrix, ord(i) - ord('A'), ord(j) - ord('A'))
            path_vertices = [chr(ord('A') + vertex) for vertex in path]
            print(f"Найкоротший шлях між {i} та {j}: \n      {shortest_distances[ord(i) - ord('A')][ord(j) - ord('A')]} "
                    f"через вершини {' -> '.join(path_vertices)}")
