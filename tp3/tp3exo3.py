for i in range(1,26):
    if 26%i != 0:
        print(i)

def affine(mot,a,b):
    list = []
    for c in mot:
        if(c != ' '):
             nbr = (ord(c)-ord('A'))
             list.append(chr((a*nbr+b) %26 + ord('A')))
        else:
            list.append(c)
    return "".join(list)


def inverse(a):
    for i in range(26):
        if((a*i)%26) == 1:
            return i
    return 0

def de_affine(code,a,b):

    list = []
    for c in code:
        if(c != ' '):
            nbr = (ord(c)-ord('A'))
            list.append(chr((inverse(a)*(nbr-b))%26 + ord('A')))
        else:
            list.append(c)
    return "".join(list)



code = affine("CE MESSAGE EST CODE",5,5)
print(code);
for i in range(26):
    if inverse(i) == 0:
        print(i , "n'est pas inversible modulo 26")
print(de_affine(code,5,5))

print(affine("CONFIDENTIEL",5,7),de_affine("RZUGVWBUYVBK",5,7))

for a in range(1,10,2):
    for b in range(10):
        print("On trouve ", de_affine("KYBIX",a,b) , "Avec a = " , a , "et b ",b)

# BRAVO avec a = 9 et b = 1

for b in range(26):
    print("on obtiens",de_affine( "LP NVP UJVR YCJAVXRJUR L PRG AP QH LJFYCPIPURXJU",15,b),"avec b =",b)

# On obtiens CE QUE NOUS PRODUISONS C EST DE LA COMPREHENSION avec b = 7