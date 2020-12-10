import sympy as sm

sm.var('n a x')

vn = sm.integrate((x**(n-1))/(a + x), (x, 0, 1))

print("vn:")
sm.pprint(vn)
print("Le resultat est inexploitable")

print("QUESTION 2:")
sm.pprint(vn.subs(n, 40))

vn = vn.subs(n, 40)
vn = vn.subs(a, 3)
sm.pprint(vn)

# QUESTION 3
for i in range(10, 60, 10):
    vn = vn.subs(n, i)
    print("vn pour i = ", i)
    sm.pprint(vn)