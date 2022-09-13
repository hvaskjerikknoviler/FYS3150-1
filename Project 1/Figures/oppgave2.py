import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fil = pd.read_table("x_u100.txt", header=None)

x=[]
u=[]

for i in range(0,len(fil[0])):
    a = fil[0][i].split()
    x.append(float(a[0]))
    u.append(float(a[1]))

plt.plot(x,u, label = "Analytisk løsning")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("Oppgave 2")
plt.savefig("oppgave2.png")
