import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,4,1)
def invest_function(n,t):
    dmdt=-k*n*t
    return dmdt
M_O=1000
inv_I=0.08
k=inv_I
solve_bk=odeint(invest_function,M_O,t)
plt.plot(t,solve_bk[:,0])
plt.show()