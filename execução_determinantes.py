import itertools
import operator
from functools import reduce

def det_4x4(matrix):
    if len(matrix) != 4 or len(matrix[0]) != 4:
        raise ValueError("A matriz não é 4x4")

    indices = [0, 1, 2, 3]
    det = 0

    for permutacao in itertools.permutations(indices):
        produto = 1
        for i in range(4):
            produto *= matrix[i][permutacao[i]]
        sinal = 1 if sum([permutacao[i] > permutacao[j] for i in range(3) for j in range(i+1, 4)]) % 2 == 0 else -1
        det += sinal * produto

    return det

m = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]
]

perm = reduce(operator.mul, (1, 2, 3, 4))
determinante = det_4x4(m)

print(f"O valor da determinante da primeira matriz é: {determinante}")

m = [
    [1, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 0, 3, 4],
    [0, 0, 0, 4]
]

determinante = det_4x4(m)

print(f"\nO valor da determinante da segunda matriz é: {determinante}")
print(f"O número de permutações possíveis em ambas matrizes é de: {perm}")