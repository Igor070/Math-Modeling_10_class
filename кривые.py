import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,4,0.11)
def invest_function(u,t):
    dmdt=f/m-y*u**2/m
    return dmdt
M_O=0
f=100
m=10
y=0.8
u=2
solve_bk=odeint(invest_function,M_O,t)
plt.plot(t,solve_bk[:,0])
plt.show()