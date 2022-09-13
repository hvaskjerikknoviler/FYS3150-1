import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fil = pd.read_table("x_v.txt", header=None)
fil1 = pd.read_table("x_u.txt", header=None)

x=[]
v=[]
x1=[]
u=[]

n = len(fil[0])
n1 = len(fil1[0])

for i in range(0,n):
    a = fil[0][i].split()
    x.append(float(a[0]))
    v.append(float(a[1]))

for i in range(0,n1):
    a = fil1[0][i].split()
    x1.append(float(a[0]))
    u.append(float(a[1]))

plt.plot(x,v, title = "Numerical approximation")
plt.plot(x1,u, title = "Analytical solution")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.savefig("figure7b")
