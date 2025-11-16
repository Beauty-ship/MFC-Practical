import sympy as sp

x, y, z = sp.symbols('x y z')

P = x**2 * y
Q = y**2 * z
R = z**2 * x

div_F = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)

print("Vector field F(x, y, z) = ⟨P, Q, R⟩")
print(f"P = {P}")
print(f"Q = {Q}")
print(f"R = {R}")
print("\nDivergence of F:")
print(f"∇·F = {div_F}")
