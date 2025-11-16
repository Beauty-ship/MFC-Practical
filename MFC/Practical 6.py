import sympy as sp

def matrix_subspace_bases(A):
    A = sp.Matrix(A)
    col_space = A.columnspace()
    row_space = A.rowspace()
    null_space = A.nullspace()
    left_null_space = A.T.nullspace()
    print("Matrix A:")
    sp.pprint(A)
    print("\n--- Bases of Fundamental Subspaces ---")
    print("\nColumn Space Basis:")
    sp.pprint(col_space)
    print("\nRow Space Basis:")
    sp.pprint(row_space)
    print("\nNull Space Basis:")
    sp.pprint(null_space)
    print("\nLeft Null Space Basis:")
    sp.pprint(left_null_space)
    return {
        "Column Space": col_space,
        "Row Space": row_space,
        "Null Space": null_space,
        "Left Null Space": left_null_space
    }
A = [
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
]

bases = matrix_subspace_bases(A)
