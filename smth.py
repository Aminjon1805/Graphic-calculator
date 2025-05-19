import numpy as np
import sympy as sp
import math


symbol_x = sp.Symbol('x')
f = "x**3"

f_s = sp.sympify(f)
numpy_f = sp.lambdify(symbol_x, f_s, modules=['numpy'])

diff_f = sp.diff(f_s)

numpy_diff_f = sp.lambdify(symbol_x, diff_f, modules=['numpy'])

x_nums = np.linspace(-10, 10, 40)

result = numpy_diff_f(x_nums)

for i in range(len(result)):
    if  0 < abs(result[i]) < 1:
        print(x_nums[i])
        print(numpy_f(x_nums[i]))

