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