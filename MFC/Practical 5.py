from numpy import matrix, linalg
import numpy as np
print("enter the dimension of coefficient matrix (A):")
NR = int(input("enter the number of rows:"))
NC = int(input("enter the number of columns:"))
print("enter the elements of coefficients matrix (A) in a single line (seperated by space):")
coefficients_entries = list(map(float, input().split()))
coefficients_matrix = np.array(coefficients_entries).reshape(NR,NC)
print("coefficient matrix (A) is as follows:",'\n',coefficients_matrix,"\n")
print("enter the elements of column matrix (B) in a single line (seperated by space):")
column_entries = list(map(float, input().split()))
column_matrix = np.array(column_entries).reshape(NR,1)
print("column matrix (B) is as follows:",'\n',column_matrix,"\n")
inv_of_coefficient_matrix = linalg.inv(coefficients_matrix)
solution_of_the_system_of_equations = np.matmul(inv_of_coefficient_matrix,column_matrix) 
print("solution of the system of eqautions using GAUSS JORDAN")
print(solution_of_the_system_of_equations)

