import math
from itertools import combinations

# Prime Number Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Sudoku Validator (3x3)
def is_valid_sudoku(board):
    def has_duplicates(values):
        nums = [v for v in values if v != '.']
        return len(nums) != len(set(nums))

    for row in board:
        if has_duplicates(row):
            return False

    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if has_duplicates(column):
            return False

    box = [board[i][j] for i in range(3) for j in range(3)]
    if has_duplicates(box):
        return False

    return True

# Vertex Cover
def is_vertex_cover(graph_edges, vertices, k):
    for subset in combinations(vertices, k):
        cover_set = set(subset)
        if all(u in cover_set or v in cover_set for u, v in graph_edges):
            return True
    return False

# Example Usage
if __name__ == '__main__':
    print("Prime Check (11):", is_prime(11))

    sudoku_board = [
        ['5', '3', '.'],
        ['6', '.', '1'],
        ['.', '9', '8']
    ]
    print("Sudoku Valid:", is_valid_sudoku(sudoku_board))

    edges = [(1, 2), (2, 3), (3, 4)]
    vertices = [1, 2, 3, 4]
    print("Vertex Cover Exists (k=2):", is_vertex_cover(edges, vertices, 2))