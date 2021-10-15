import numpy as np
from tictactoe import *
matrix = np.array(
         [[-2,  5,  3,  2, 2, 3, 4, 5, 2, 1],
          [ 9, -6,  5,  1, 2, 3, 4, 5, 6, 8],
          [ 3,  2,  7,  3, 5, 4, 3, 2, 6, 7],
          [-1,  8, -4,  8, 4, 7, 2, 4, 7, 9],
          [1, 2, 3, 4, 5, -6, 4, 3, 3, 5],
          [-2, 5, 3, 2, 2, 3, 4, 5, 2, 1],
          [9, -6, 5, 1, 2, 3, -4, 5, 6, 8],
          [3, 2, 7, 3, 5, 4, 3, 2, 6, 7],
          [-1, 8, -4, 8, 4, 7, 2, -4, 7, 9],
          [1, 2, 3, 4, 5, 6, 4, 3, 3, 5],
          ])

matrix2 = [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]]

diags = [matrix[::-1,:].diagonal(i) for i in range(-9,10)]
diags.extend(matrix.diagonal(i) for i in range(9,-10,-1))
tmp = []
for i in diags:
    if len(i) >= 5:
        # print(split_ls(i, 5)[0:])
        for j in (split_ls(i, 5)[0:]):
            matrix2.append(list(j))

for i in matrix2:
    print(i)






