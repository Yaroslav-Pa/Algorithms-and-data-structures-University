from collections import deque
from variables3 import matrix, goal
def find_start_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is None:
                return i, j
                
def find_path_bfs(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])
    
    def get_neighbors(cell):
        r, c = cell
        neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        return [(nr, nc) for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols]

    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            # if neighbor not in visited:
            # if matrix[neighbor[0]][neighbor[0]] is not None:
                queue.append((neighbor, path + [neighbor]))

    return None

start = find_start_position(matrix)

path_bfs = find_path_bfs(matrix, start, goal)
print("Початкова матриця:")
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}")
print(f"Ціль: {goal}")
print("Шлях:", path_bfs)
