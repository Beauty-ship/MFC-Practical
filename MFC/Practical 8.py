import numpy as np

def gram_schmidt(vectors):
    vectors = [np.array(v, dtype=float) for v in vectors]
    orthogonal = []
    
    for v in vectors:
        for u in orthogonal:
            v = v - np.dot(v, u) / np.dot(u, u) * u
        orthogonal.append(v)

    orthonormal = [u / np.linalg.norm(u) for u in orthogonal if np.linalg.norm(u) != 0]

    print("\nOrthogonal basis:")
    for u in orthogonal:
        print(u)

    print("\nOrthonormal basis:")
    for e in orthonormal:
        print(e)

    return orthonormal
if __name__ == "__main__":
    v1 = [1, 1, 0]
    v2 = [1, 0, 1]
    v3 = [0, 1, 1]
    vectors = [v1, v2, v3]

    print("Given vectors:")
    for v in vectors:
        print(v)

    orthonormal_basis = gram_schmidt(vectors)
