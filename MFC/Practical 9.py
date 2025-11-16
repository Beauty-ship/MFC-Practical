import numpy as np

def check_diagonalizable(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Matrix A:\n", A)
    print("\nEigenvalues:\n", eigenvalues)
    print("\nEigenvectors:\n", eigenvectors)
    rank = np.linalg.matrix_rank(eigenvectors)
    n = A.shape[0]

    if rank == n:
        print("\n✅ The matrix is diagonalizable.")
    else:
        print("\n❌ The matrix is NOT diagonalizable.")

    return eigenvalues, eigenvectors

def verify_cayley_hamilton(A):
    n = A.shape[0]
    coeffs = np.poly(A) 

    print("\nCharacteristic polynomial coefficients:")
    print(coeffs)
    result = np.zeros_like(A, dtype=float)

    for i, c in enumerate(coeffs):
        power = n - i
        term = c * np.linalg.matrix_power(A, power)
        result += term

    print("\nMatrix substitution result (should be close to zero):\n", result)
    if np.allclose(result, np.zeros_like(A)):
        print("\n✅ Cayley-Hamilton theorem verified!")
    else:
        print("\n❌ Cayley-Hamilton theorem failed (numerical error likely if small).")

if __name__ == "__main__":
    A = np.array([[4, 1],
                  [2, 3]], dtype=float)

    eigenvalues, eigenvectors = check_diagonalizable(A)
    verify_cayley_hamilton(A)
