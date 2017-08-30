import numpy as np

sudoku = np.arange([[1,9],[1,9]])
a = np.array([[1, 2], [1, 2]])
print(a.shape)

# indexing with np.newaxis inserts a new 3rd dimension, which we then repeat the
# array along, (you can achieve the same effect by indexing with None, see below)
b = np.repeat(sudoku[:, :, np.newaxis], 3, axis=2)

print(b.shape)
# (2, 2, 3)

print(b[:, :, 0])
# [[1 2]
#  [1 2]]

print(b[:, :, 1])
# [[1 2]
#  [1 2]]


print(sudoku)