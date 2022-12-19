"""
5. Решить обыкновенное дифференциальное уравнение. Решение представить в табличной и графической формах. Для оценки погрешности выполнить расчёт с шагом h и с шагом h/2.
Задание:
По формуле 4-го порядка точности решить дифференциальное уравнение методом Адамса:
 y'=y-2*x/y                   
 y(0)=1; h=0,2; 0<=x<=2; нач. отр. [1;1,1832;1,3416;1,4832]


"""


import numpy as np
import matplotlib.pyplot as plt

# Function to compute the derivative at a given step
def f(x, y):
  return y - 2*x/y

# Initialize variables
x = 0
y = 1
h = 0.2

# Arrays to store the solutions and errors
x_values = []
y_values = []
errors = []

# Iterate through the values of x
while x <= 2:
  # Append the current solution to the arrays
  x_values.append(x)
  y_values.append(y)

  # Use Adams method to compute the solution at the next step
  y_h = y + h/24 * (55*f(x, y) - 59*f(x-h, y-h*f(x-h, y)) + 37*f(x-2*h, y-2*h*f(x-2*h, y)) - 9*f(x-3*h, y-3*h*f(x-3*h, y)))

  # Use Adams method to compute the solution with a step size of h/2
  y_h2 = y + h/2/24 * (55*f(x, y) - 59*f(x-h/2, y-h/2*f(x-h/2, y)) + 37*f(x-h, y-h*f(x-h, y)) - 9*f(x-3*h/2, y-3*h/2*f(x-3*h/2, y)))

  # Calculate the error as the absolute difference between the two solutions
  error = abs(y_h2 - y_h)
  errors.append(error)

  # Update the value of y and x
  y = y_h
  x = x + h

# Plot the solution and the error on the same graph
plt.plot(x_values, y_values, label='Solution')
plt.plot(x_values, errors, label='Error')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
