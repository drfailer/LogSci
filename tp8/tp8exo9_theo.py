import numpy as np
from scipy.integrate import quad

# Fonction de test :
def sin(x):
 return np.sin(x)

# Méthode des rectangles à gauche :
def int_rect_g(f,a,b,n):
 c = np.linspace(a,b,n+1)
 c = c[:n]
 c = (b-a)/n * f(c);

 return sum(c);

# Méthode des rectangles à droite :
def int_rect_d(f,a,b,n):
 c = np.linspace(a,b,n+1)
 c = c[1:]
 c = (b-a)/n * f(c);

 return sum(c);

# Méthode des trapèzes :
def int_rect_t(f,a,b,n):
 c = np.linspace(a,b,n+1)
 c = ((b-a)/n)*(f(c[1:])+f(c[:n]))/2;

 return sum(c);

# Tests :
for i in range(1,7):
 print(int_rect_g(sin,0,np.pi/2,10**i))
 print(int_rect_d(sin,0,np.pi/2,10**i))
 print(int_rect_t(sin,0,np.pi/2,10**i))
 print("-----------------------------")
 print(quad(sin,0,np.pi/2))
