import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,100,1)
def bak_function(n,t):
    dmdf=k*n
    return dmdf
M_O=10
bak_I=0.05
k=bak_I
solve_bk=odeint(bak_function,M_O,t)
plt.plot(t,solve_bk[:,0])
plt.show()