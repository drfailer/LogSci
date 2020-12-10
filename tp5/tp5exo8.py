import sympy as sm

sm.var('x')

f = 1/2 * x**2 + x -1
t = sm.diff(f, x).subs(x, 2) * (x - 2) + f.subs(x, 2)

sm.plot(f, t, (x, -10, 10))
