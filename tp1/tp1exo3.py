import numpy as np

x = 20

print("Log(x) = ", np.log10(x), "\n", "sin = ", np.sin(x))
#######################################
print(np.sin(np.pi ** 2))
print(np.log(2021))
#######################################
list = [90, 99, 101, 120, 999, 500, 1001]
for i in list:
    print(np.log10(i))
# La partie entiere du log10 donne le nombre de digit -1 de la partie entiere du nombre d'origine
#######################################
x = (2 ** 64) - 1
print(int(np.log10(x)) + 1)
################
print(int(234 * np.log10(123)) + 1)
