def code_une(lt):
    return ord(lt) - ord('A')



def decode_une(c):

    return chr(c + ord('A'))


def  code_mot(m):
    l = []
    l = list(map(code_une,m))

    return l

def decode_mot(l):
    m = list(map(decode_une,l))
    s = "".join(m)
    return s




s = "CESAR"
c = [2,4,18,0,17]
for i in s:
    print(code_une(i))

print(code_mot(s))

for i in c:
    print(decode_une(i))



print(decode_mot(c))

