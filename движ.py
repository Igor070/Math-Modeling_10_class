from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

n = 100

phi = np.linspace(0, 2 * np.pi, n)
theta = np.linspace(0, 8 * np.pi, n)

h = 0.5

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = h * np.outer(np.ones(np.size(phi)), theta)
ax.plot_surface(x, y, z, color='w')

x1 = phi * np.cos(theta)
y1 = phi * np.sin(theta)
z1 = h * theta


ball, = ax.plot(x1, y1, z1, 'o', color='b')
line, = ax.plot(x1, y1, z1, '-', color='r')

def animation_func(i):
    ball.set_data(x1[i], y1[i])
    ball.set_3d_properties(z1[i])
    
    line.set_data(x1[:i], y1[:i])
    line.set_3d_properties(z1[:i])
    
ax.set_xlim3d([-7.0, 7.0])
ax.set_xlabel('X')
    
ax.set_ylim3d([-7.0, 7.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-7.0, 7.0])
ax.set_label('Z')

ani = animation.FuncAnimation(fig, animation_func, n, interval=50)
ani.save('ani.gif')