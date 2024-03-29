import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Definerer tekstfiler
fil = pd.read_table("x_v10.txt", header=None)
fil1 = pd.read_table("x_u10.txt", header=None)
fil2 = pd.read_table("x_v100.txt", header=None)
fil3 = pd.read_table("x_u100.txt", header=None)
fil4 = pd.read_table("x_v1000.txt", header=None)
fil5 = pd.read_table("x_u1000.txt", header=None)

#Definerer tomme lister som skal fylles
x10=[]
v10=[]
u10=[]

x100=[]
v100=[]
u100=[]

x1000=[]
v1000=[]
u1000=[]


#Funksjon for å fylle listene og regne ut logerror og relativ error
def append(x, u, v, fil, fil1):
    n = len(fil[0])

    for i in range(0,n):
        a = fil[0][i].split()
        x.append(float(a[0]))
        v.append(float(a[1]))

        b = fil1[0][i].split()
        u.append(float(b[1]))

    logerror = np.zeros(n)
    relerror = np.zeros(n)
    for i in range(1,n-1):
        logerror[i] = np.log(np.abs(u[i]-v[i]))
        relerror[i] = np.log(np.abs((u[i]-v[i])/u[i]))

    return x, u, v, logerror, relerror

#Definerer verdier for forskjellige n
x10, u10, v10, logerror10, relerror10 = append(x10, v10, u10, fil, fil1)
x100, u100, v100, logerror100, relerror100 = append(x100, v100, u100, fil2, fil3)
x1000, u1000, v1000, logerror1000, relerror1000 = append(x1000, v1000, u1000, fil4, fil5)

#Plotting av v, u og error
plt.plot(x10,v10, label="n=10")
plt.plot(x100,v100, label="n=100")
plt.plot(x1000,v1000, label="n=1000")
plt.plot(x100,u100, "k--", label="Analytical")
plt.title("Analytical plot vs numerical with different valued n")
plt.xlabel("x")
plt.ylabel("v(x)")
plt.legend()
plt.grid()
plt.savefig("figure7b")
plt.show()


plt.plot(x10, logerror10, label="n = 10")
plt.plot(x100, logerror100, label="n = 100")
plt.plot(x1000, logerror1000, label="n = 1000")
plt.title("Absolute error")
plt.xlabel("x")
plt.ylabel("Absolute error(u, v)")
plt.grid()
plt.legend()
plt.savefig("figure8a")
plt.show()

plt.plot(x10, relerror10, label="n = 10")
plt.plot(x100, relerror100, label="n = 100")
plt.plot(x1000, relerror1000, label="n = 1000")
plt.title("Relative error")
plt.xlabel("x")
plt.ylabel("Relavtive error(u, v)")
plt.grid()
plt.legend()
plt.savefig("figure8b")
plt.show()
