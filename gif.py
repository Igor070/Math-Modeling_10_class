import numpy as np
import matplotlib. pyplot as plt
from matplotlib. animation import FuncAnimation
fig, ax=plt.subplots()
ball,=plt.plot([],[],marker='o',color='r')
def circle_plotter(R,t):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    return x,y
edge=10
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(i):
    ball.set_data(circle_plotter(R=5,t=i))
ani=FuncAnimation(fig,animate,frames=1000,interval=300) 
ani.save('animat.gif')
