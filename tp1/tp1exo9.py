def syracuse(n):
    s = 1
    while n != 1 :
        if n % 2 == 0:
            n /= 2
        else :
            n = (n*3+1)/2
        s += 1
    return s 

#######################

print(syracuse(10),syracuse(100))

#######################

for i in range(10,26):
    print("la première occurrence de 1 dans la suite de syracuse avec",i,"comme argument est :",syracuse(i))

#######################

lmax,max = -1,-1
for i in range(10,10000):
    if lmax < syracuse(i):
        lmax = syracuse(i)
        max = i
print("la longueur de sycaruse est maximale lorsque",max,"est l'argument, donnant une longueur de :",lmax)
