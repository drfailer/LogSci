import numpy as np

A = np.array([[6,2,8,0],
             [3,0,1,8],
             [7,4,0,3],
              [2,6,7,0]])

B = np.array(range(1,5))

############### Inverse


A1 = np.linalg.inv(A)

x = A1@B

print("On a donc comme solution avec la matrice inverse :")
print(x)

############### Solve

x = np.linalg.solve(A,B)
print("On a donc comme solution avec solve :")
print(x);


############### Cramer

d = np.linalg.det(A)

for i in range(4):
    Ac = np.copy(A)
    Ac[:,i] = B
    dc = np.linalg.det(Ac)
    x[i] = float(dc/d)

print("On a donc comme solution avec Cramer :")
print(x);
    
    
