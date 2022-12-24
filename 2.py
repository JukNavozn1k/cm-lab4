import math
from tabulate import tabulate

# Function to be integrated
def f(x):
  return math.log(x + 2) / x

# Integration limits
a = 1.2
b = 2
accuracy = 1E-6
# Initial step size
h = math.exp(1 / 2)

# Initial estimate of the integral using the trapezoid rule
n = int((b - a) / h)
x = [a + i * h for i in range(n + 1)]
y = [f(x_i) for x_i in x]
integral = h / 2 * sum(y[i] + y[i+1] for i in range(n))

# Create a table to store the results
results = []

# Loop until the error is within the required tolerance
while True:
  # Calculate the error using Runge's principle
  h /= 2
  n = int((b - a) / h)
  x = [a + i * h for i in range(n + 1)]
  y = [f(x_i) for x_i in x]
  integral_new = h / 2 * sum(y[i] + y[i+1] for i in range(n))
  error = abs(integral - integral_new) / 3

  # Add the results to the table
  results.append([h, integral_new, error])

  # Check if the error is within the required tolerance
  if error < accuracy:
    break
  
  # Update the integral estimate
  integral = integral_new

# Print the results in a table
print(tabulate(results, headers=["Step size", "Integral", "Error"]))
