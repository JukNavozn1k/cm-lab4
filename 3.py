import numpy as np
from tabulate import tabulate

def func(x):
    return x**2 / np.sqrt(x**2 + 1)

# Gauss quadrature formula with 5 nodes
n1 = 5
x1 = np.array([-0.90618, -0.538469, 0, 0.538469, 0.90618])
A1 = np.array([0.23698, 0.47863, 0.56889, 0.47863, 0.23698])

# Generate table for 5 nodes
table1 = []
for i in range(n1):
    table1.append([x1[i], A1[i]])
print(tabulate(table1, headers=['x', 'A'], floatfmt=".10f"))

# Calculate definite integral with 5 nodes
a = -0.5
b = 1.3
integral1 = 0
for i in range(n1):
    integral1 += A1[i] * func((b - a) / 2 * x1[i] + (b + a) / 2)
integral1 *= (b - a) / 2
print("Definite integral with 5 nodes:", integral1)

# Gauss quadrature formula with 8 knots
n2 = 8
x2 = np.array([-0.96028986, -0.79666648, -0.52553242, -0.18343464, 
               0.18343464, 0.52553242, 0.79666648, 0.96028986])
A2 = np.array([0.10122854, 0.22238103, 0.31370664, 0.36268378, 
               0.36268378, 0.31370664, 0.22238103, 0.10122854])

# Generate table for 8 nodes
table2 = []
for i in range(n2):
    table2.append([x2[i], A2[i]])
print(tabulate(table2, headers=['x', 'A'], floatfmt=".10f"))

# Calculate definite integral with 8 nodes
integral2 = 0
for i in range(n2):
    integral2 += A2[i] * func((b - a) / 2 * x2[i] + (b + a) / 2)
integral2 *= (b - a) / 2
print("Definite integral with 8 nodes:", integral2)
