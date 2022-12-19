'''

1. Вычислить определённый интеграл с точностью до 0,0001. Выбрать значение n, обеспечивающее заданную точность, из формулы остаточного члена.
Задание:
Определённый интеграл от функции:   1/sqrt(2*x^2+1)              
Пределы интегрирования:  [0,8;1,6]    
Использовать формулу Симпсона.


'''


import math

def f(x):
  return 1/math.sqrt(2*x**2 + 1)

def simpson(a, b, n):
  h = (b - a) / n
  x0 = a
  xn = b
  result = f(x0) + f(xn)

  for i in range(1, n, 2):
    result += 4 * f(a + i * h)

  for i in range(2, n-1, 2):
    result += 2 * f(a + i * h)

  result *= h / 3
  return result

a = 0
b = 8
n = 100  # choose a value for n that gives the desired accuracy
result = simpson(a, b, n)
print(result)
