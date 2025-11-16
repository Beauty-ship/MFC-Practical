import numpy as np
NR = int(input("enter the number of rows:"))
NC = int(input("enter the number of columns:"))
print("enter the entries in a single line (seperated by space):")
entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(NR,NC)
print("matrix X is as follows:",'/n', matrix)
print("the rank of a matrix is:",np.linalg.matrix_rank(matrix))