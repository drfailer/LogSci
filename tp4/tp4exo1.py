import matplotlib.pyplot as plt
import numpy as np

def fibo(n):
	f_n = n
	f_n1 = 1
	f_n2 = 0
	if n >= 2:
		for i in range(2,n):
			f_n = f_n2 + f_n1
			f_n2 = f_n1
			f_n1 = f_n

	return f_n



l = [x for x in range(26)]
f = []
for i in l:
	f.append(fibo(l[i]))
plt.plot(l, f)
plt.yscale("log")
plt.show()


# un equivalent de cette suite est log(10^x)