from sympy import solve, Float, var

var('x y z')
p = 3*x**2 - (7*x**2)/2 - x/2 + 1
s = solve(p,x)
for i in s:
    print("p est résolu lorsque x = :",i)
    print('Vérification : p(',i,') =',p.subs(x,i))

print("Question2 :")
print('la solution de cette matice est :',solve([2*y+5*z-3,-3*x+2*y-z+1,-x+2*y+2*z-5],[x,y,z]))