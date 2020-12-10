import sympy as sm

sm.var('x n')

# QUESTION 1

l1 = sm.limit(sm.sqrt(x**2 + 1) - sm.sqrt(x**2 + 1), x, sm.oo)

print("limite 1: ", l1)

l2 = sm.limit((1 + 5 / (3*n))**(2*n), n, sm.oo)

print("limite 2: ", l2)

# QESTION 2

F = sm.integrate(x / (1 + sm.sqrt(x)), x)
G = sm.integrate(3*x * sm.sqrt(1 + x**2), x)

print("Primitive de f: ")
sm.pprint(F)
print("Dérivée de F: ")
sm.pprint(sm.diff(F, x))

print("Primitive de g: ")
sm.pprint(G)
print("Dérivée de G: ")
sm.pprint(sm.diff(G, x))

# QUESTION 3

I = sm.integrate((x * sm.log(sm.sqrt(x**2 + 3))) / sm.sqrt(x**2 + 3))
# I = sm.integrate((x * sm.log(sm.sqrt(x**2 + 3))) / sm.sqrt(x**2 + 3),(x,1,2))
print("Integrale (q3): ", I)
