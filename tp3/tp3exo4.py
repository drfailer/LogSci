
import math

def euler(n):
    if n == 0:
        return 1
    else :
        return euler(n-1)+1/math.factorial(n)


print(euler(20))