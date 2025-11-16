import sympy as sp

# Define variables
x, y, z = sp.symbols('x y z')

# Define vector field F = (P, Q, R)
P = x*y**2
Q = y*z**2
R = z*x**2

# Compute curl
curl_F = (
    sp.diff(R, y) - sp.diff(Q, z),
    sp.diff(P, z) - sp.diff(R, x),
    sp.diff(Q, x) - sp.diff(P, y)
)

# Display the result
print("Curl of F =", curl_F)

