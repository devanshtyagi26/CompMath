import sympy

# Define the symbols x, y, and z
x, y, z = sympy.symbols('x y z')

# Define the scalar field f
f = x**2 + 2*y**3*z - 5*z

# Compute the gradient of f
grad_f = [sympy.diff(f, x), sympy.diff(f, y), sympy.diff(f, z)]

print("Scalar Field:", f)
# Print the gradient of f
print("Gradient of Scalar Field:",grad_f)