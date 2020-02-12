from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation  

fig=plt.figure()
ax=p3.Axes3D(fig)

N=19999999999999990

phi=np.linspace(10,np.pi)
theta=np.linspace(8,np.pi)

x1=1*np.outer(np.cos(phi),np.sin(theta))
y1=1*np.outer(np.sin(phi),np.sin(theta))
z1=1*np.outer(np.ones(np.size(phi)),np.sin(theta))

ax.plot_surface(x1,y1,z1,color='w')

x=1*np.cos(phi)*np.sin(theta)
y=1*np.sin(phi)*np.sin(theta)
z=1*np.sin(theta)

ball,=ax.plot(x,y,z,'o',color='r')
line,=ax.plot(x,y,z,'-',color='b')

def animation_func(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])
    
ax.set_xlim3d([-1.0,1.0])
ax.set_xlabel('X')
    
ax.set_ylim3d([-1.0,1.0])   
ax.set_ylabel('Y')   

ax.set_zlim3d([-1.0,1.0])   
ax.set_zlabel('Z') 
      
ani=animation.FuncAnimation(fig, animation_func, N , interval=10)

ani.save('ani.gif')
