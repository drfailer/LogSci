# Question 1
def pgcd(a, b):
    if a > b:
        c = b
        b = a
        a = c

    while b % a !=0:
        r = b % a
        b = a
        a = r

    return a 

print('Question 2:')
print('pgcd(495, 275) = ', pgcd(495, 275))
