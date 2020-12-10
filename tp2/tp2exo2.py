import numpy as np

def suite_vn(n, a):
    if n == 1:
        return np.log((1 + a) / a)
    else:
        return 1/(n-1) - a * suite_vn(n-1,a)

##########################################
print(suite_vn(40, 3))
# Résultat: 253.08061664510203
# Ce résultat n'est pas compris entre 1/(n(a+1) et 1/(na), il est donc faux


##########################################
def suite_vn_2(n, a, u_start, n_start):
    for i in range(n_start - n):
        u_start = -(u_start - 1/(n - 1)) / a
    return u_start

print(suite_vn_2(40, 3, 882415619420.4503, 60))
