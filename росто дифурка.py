import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,27,0.01)

def diff_function(z,t):
    y,s=z
    dy_dt=s
    ds_dt=-np.sin(y)*s-3*y*t-5
    return dy_dt,ds_dt
y_0=0.01
s_0=0.05
z0=y_0,s_0
sol=odeint(diff_function,z0,t)
plt.plot(sol[:,1],sol[:,0])
plt.legend()
plt.show()

