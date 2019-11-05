import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=1,b=2,c=3,k=13,title='Parabola_plotter'):
    """ рисуем пораболу 
    """
    x=np.arange(-15,15,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y,label="parabola")
    plt.plot (x,y,color='m')
    x=np.arange(0.1,11,0.01)
    y=k/x
    plt.plot(x,y,label="parabola")
    plt.plot (x,y,color='g')
    plt.show()
parabola_plotter()
