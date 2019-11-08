import matplotlib.pyplot as plt
import numpy as np
def kryg_plotter(r=3,titel='kryg_plotter'):
    """
    рисуем окружность
    """
    x=np.arange(-5,5,0.01)
    y=np.arange(-5,5,0.01)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[r**2])
    plt.show()
kryg_plotter(4)  