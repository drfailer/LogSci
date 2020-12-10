def suite_x(n):
    if n == 0:
        return 0.23
    else:
        xn = suite_x(n - 1)
        return 4 * xn * (1 - xn)

print(suite(10), suite(60))
#0.010842573398723198 0.42147357550640646

def suite_y(n):
    if n == 0:
        return 0.23
    else:
        yn = suite_y(n-1)
        return 4 * yn - 4 * yn ** 2

print(suite_y(10),suite_y(60))
#0.010842573398724298 0.7316081731057733

##########################################
# Mathématiquement, ces deux formules sont équivalentes, cependant, le programme
# trouve des résultats différents. Cela s'explique par le fait que l'ordinateur
# manipule des variables flottantes inexacte et donc accumule une multitude
# d'erreurs de précisions ce qui donne un résultat faux avec les deux formules.
##########################################
