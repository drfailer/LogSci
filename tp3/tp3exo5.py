


from time import time
import datetime

def harmonique(n):
    if n == 0:
        return 0
    else:
        return harmonique(n-1) + 1/n

def fibo_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo_r(n-1) + fibo_r(n-2)


print(harmonique(100),harmonique(950))
temps = 1

for n in range(25,36):
    t_start = time()
    fibo_r(n)
    t_fin = time()
    print("temps d’execution", t_fin-t_start, "sec.")
    print("difference :",(t_fin - t_start)  / temps  )
    temps = t_fin - t_start

#♦fibo(80) mettra environ 5 jours, 5 heures et 56 secondes
#♦fibo(120) mettra environ 158 980 614 ans



