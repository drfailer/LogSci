import matplotlib.pyplot as plt
import numpy as np

a = 2.1
x = 0.2
L = []

# QUESTION 1
for i in range(1,211) :
    x = a*x*(1-x)
    if i > 200 :
        L.append(x)
        print("x est égale à :" , x , "lorsque i =" , i)


# Rep 1: On obtient toujours la même valeur


# QUESTION 2

a = 3.1
x = 0.2
L = []

for i in range(1,211) :
    x = a*x*(1-x)
    if i > 200 :
        L.append(x)


print('q2: ', L)

plt.plot([i for i in range(201,211)],L,'.')
plt.figure()

# Rep 2: ossilation entre 2 val

# QUESTION 3

a = 3.46
x = 0.2
L = []
A = []

for i in range(1,211) :
    x = a*x*(1-x)
    if i > 200 :
        L.append(x)
        A.append(a)


plt.plot(A, L, '.')
plt.figure()


# Rep 3: on voit 4 points

x = 0.2
L = []
A = []
for a in range(250, 400):
    for i in range(200, 300):
        x = (a/100)*x*(1-x)
        L.append(x)
        A.append(a)

plt.plot(A, L, '.', color='r', markersize=1)


plt.show()
