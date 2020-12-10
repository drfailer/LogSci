import sympy as sm

sm.var('a b c')
sm.var('x u v w h')

p = a*x**2 +b*x + c

p = p.subs(a, v - (w - h**2 * v) / (-h**3 + 2*h))
p = p.subs(b, v - (w - v*h**2) / (-h**2 + 2) -u)
p = p.subs(c, u)

sm.pprint(p)

p = p.subs(u, 0)
p = p.subs(v, 2)
p = p.subs(w, 1)
p = p.subs(h, 2)

sm.pprint(p)