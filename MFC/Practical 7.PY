import numpy as np

def check_linear_dependence(vectors):
    mat = np.column_stack(vectors)  
    rank = np.linalg.matrix_rank(mat)
    n_vectors = mat.shape[1]

    print("\nMatrix of vectors:\n", mat)
    print("Rank:", rank)
    print("Number of vectors:", n_vectors)

    if rank < n_vectors:
        print("=> The vectors are linearly DEPENDENT.")
    else:
        print("=> The vectors are linearly INDEPENDENT.")

def linear_combination(vectors, coefficients):
    result = sum(c * v for c, v in zip(coefficients, vectors))
    print("\nLinear combination result:", result)
    return result

def transition_matrix(B, C):
    B_mat = np.column_stack(B)
    C_mat = np.column_stack(C)
    P = np.linalg.inv(B_mat) @ C_mat
    print("\nTransition matrix from B to C:\n", P)
    return P
if __name__ == "__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([2, 4, 6])
    v3 = np.array([1, 0, 1])
    
    vectors = [v1, v2, v3]
    check_linear_dependence(vectors)

    linear_combination(vectors, [2, -0.5, 3])
    B = [np.array([1, 0]), np.array([0, 1])]     
    C = [np.array([1, 1]), np.array([1, -1])]   
    transition_matrix(B, C)
