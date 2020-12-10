def cesar(ph,dec):
    l = []
    for i in ph:
        l.append(decalage_une(i,dec))
    return "".join(l)


def decesar(ph,dec):
    l = []
    for i in ph:
        l.append(decalage_une(i,-dec))
    return "".join(l)


def decalage_une(c,dec):
    if(c != ' '):
        a = (ord(c)-ord('A')+dec) % 26

        return chr(a+ord('A'))
    else:
        return c




ph = "CESAR C EST GENIAL"
print(cesar(ph,3))
print(decesar('FHVDU F HVW JHQLDO',3))

ph = "CE MESSAGE EST CONFIDENTIEL"
print(cesar(ph,10))
print(decesar('MO WODDKQO ODE MYXPSNOXESOV',10))
for i in range(25):
    print('avec i =',i,'on obtiend',decesar('KYV RIK FW GIFXIRDDZEX ZJ KYV RIK FW FIXREZQZEX TFDGCVOZKP',i, ))

