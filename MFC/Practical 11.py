import sympy as sp

x, y, z = sp.symbols('x y z')

f = x**2 * y + 3*y*z - sp.sin(x*z)

grad_f = [sp.diff(f, var) for var in (x, y, z)]

print("Scalar field f(x, y, z) =", f)
print("\nGradient of f:")
for i, g in zip(('∂f/∂x', '∂f/∂y', '∂f/∂z'), grad_f):
    print(f"{i} = {g}")
