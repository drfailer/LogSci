from sympy import evalf, Float

x = Float(0.23)
for i in range (1,61):
    x = (4*x*(1 - x)).evalf(500)
    if (i%10 == 0):
        print(x.evalf(20))
print("##########################################")
x = Float(0.23)
for i in range (1,61):

    x = (4*x - 4*x**2).evalf(500)
    if (i%10 == 0):
        print(x.evalf(20))

# On obtient des résultats similaires car la précision est plus grande ici (500 chiffre après la virgule)