import sympy as sm

sm.var('x')

# On decompose la fonction en deux fonction u et v

u = sm.sqrt(x**2 + 3)
print("u:")
sm.pprint(u)
print("du / dx:")
sm.pprint(sm.integrate(u, x))

v = sm.log(sm.sqrt(x**2 + 3))
print("v:")
sm.pprint(v)
print("dv / dx:")
sm.pprint(sm.integrate(v, x))

# la fonction s'écrit sous la forme u'v

print("f:")
sm.pprint(sm.diff(u, x) * v)

# la primitive de la fontion est donc uv - integrate(v'u)

sm.pprint(sm.integrate(sm.diff(u*v, x), x) - sm.integrate(sm.diff(v, x)*u, x))
print("integrale: ", sm.integrate(sm.diff(u*v, x), (x, 0, 1)) - sm.integrate(sm.diff(v, x)*u, (x, 0, 1)))