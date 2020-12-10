def div35(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


print(div35(1000),div35(2000)+div35(3000))