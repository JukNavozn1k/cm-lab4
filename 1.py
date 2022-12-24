import math
from tabulate import tabulate

def simpson(f, a, b, n):
    """
    Approximate the definite integral of the function f(x) over the interval [a, b] using the Simpson's rule.
    """
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)
    return result * h / 3

def f(x):
    """
    The function to be integrated.
    """
    return 1 / math.sqrt(2*x**2 + 1)

# Set the integration limits and desired accuracy
a, b = 0, 100
# Compute the definite integral using the Simpson's rule for different values of n
n = 10
accuracy = 0.0001

# Initialize the tables to store the results
results = []
residuals = []



while True:
    result = simpson(f, a, b, n)
    h = (b - a) / n
    residual = (b - a) * h**4 / (180 * n**4) * max(abs(f(x)) for x in [a, b])
    results.append(result)
    residuals.append(residual)
    
    # Print the results and residual terms at each iteration
    print(f"n = {n}, Result = {result:.4f}, Residual term = {residual:.4e}")
    
    # If the residual term is less than the desired accuracy, break the loop
    if abs(residual) < accuracy:
        break 
    n *= 2

# Print the results in a table using the tabulate library
headers = ["n", "Result", "Residual term"]
table = [headers] + list(zip(range(10, n+1, 10), results, residuals))
print(tabulate(table, headers="firstrow", floatfmt=".4f"))
