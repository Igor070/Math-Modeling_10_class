import numpy as np
import matplotlib.pyplot as plt
def kryg_plotter(R=6,titel='kryg plotter'):
    t=np.arange(-11*np.pi,11*np.pi,0.1)
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    plt.plot (x,y)
    plt.show()
kryg_plotter()