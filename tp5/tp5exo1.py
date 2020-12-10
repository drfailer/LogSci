from sympy import var, expand, factor, ratsimp,together, Rational, pprint, apart,simplify, cos, sin, sqrt, evalf


var('x y z')
print(x + y + 2*x + z + 1)
print("Question1 :", expand((x-1)*(x-2)*(x-3)))
print("Question2 :", factor(x**3 - 39*x - 70))
print("Question3 :")
pprint(ratsimp(1/(x+1) + 1/y + 1/z))
print("Question4 :")
pprint(apart((2*x**2 + 4*x + 3)/(x**3 - 39*x - 70)))
print("Question5 :")
print(simplify(cos(x+y)+cos(x-y)+sin(x+y)+sin(x-y)))
print("Question6 :")
p = 2*x**2 - 3*x + 1
print("La solution de p en 5 est :", p.subs(x,5))
print("p(y + 1) - p(y - 1) :", simplify(p.subs(x,y+1)-p.subs(x,y-1)))
print("Question7 :", sqrt(10).evalf())





