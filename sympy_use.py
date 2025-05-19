import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# "np": np np.cos
# x = sp.Symbol('x')
# f = sp.cos(x) + 3*x
#
# f_prime = sp.diff(f, x)
# print(f_prime)

# smth = "cos(x) + 2*x"
# expr = sp.sympify(smth)
# x = sp.Symbol('x')
# f = sp.diff(expr)
# f_2 = sp.integrate(expr, (x, 0, 2))
# print(f)
# print(str(f))
#
# print(f_2)
# print(sp.diff(sp.simplify('x')) == sp.sympify("1"))
#
# y_diff = sp.diff(sp.sympify("x"))
# print(y_diff == sp.sympify("1"))

# f_integ = sp.lambdify(x, f, modules=['numpy'])
# print(f_integ)
#
# x = np.linspace(1, 10, 40)
#
#
# solve = sp.solve(f_integ, x)

#
# formula = "cos(x)"
# f = sp.sympify(formula)
# diff_f = sp.diff(f)
# x = sp.Symbol('x')
#
# f_lambdify = sp.lambdify(x, f, modules=['numpy'])
# diff_f_lambdify = sp.lambdify(x, diff_f, modules=['numpy'])
#
# x = np.linspace(-10, 10, 40)
# y = f_lambdify(x)
# diff_y = diff_f_lambdify(x)
#
# critical_x = []
#
# for i in range(len(diff_y)):
#     if abs(diff_y[i]) < 0.01:
#         critical_x.append(x[i])
#
#


a = [1,2,3,1,4,5,4,5,5,6,6,7,8,9,10]
print(list(set(a)))




