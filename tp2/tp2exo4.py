def fibo_liste(n):
    liste = []
    liste.append(0)
    liste.append(1)
    for i in range(2, (n + 1), 1):
        fn = liste[i - 1] + liste[i - 2]
        liste.append(fn)

    return liste


def fibo(n):
    f_nm2 = 0 # f_(n-2)
    f_nm1 = 1 # f_(n-1)
    for i in range(2, (n + 1), 1):
        f_n = f_nm2 + f_nm1
        f_nm2 = f_nm1
        f_nm1 = f_n

    return f_n


#########################################
# Question 1
print('Question 1:')
li = fibo_liste(20)
print(li)

# Question 2
print('\nQuestion 2:')
print(fibo(20))

# Question 3
s = 0
f_nm2 = 0 # f_(n-2)
f_nm1 = 1 # f_(n-1)
for i in range(2, 10 ** 5, 1):
    f_n = f_nm2 + f_nm1
    f_nm2 = f_nm1
    f_nm1 = f_n    
    if f_n % 2 == 0:
        s += f_n

print('\nQuestion 3:')
print(s % 10000007)
