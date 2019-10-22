from constant_modul import  G
from math import cos,pi
h=100 
b=30
a=pi/3
u=((G*h*cos(b)**2)/2*cos(a)**2*(1-cos(b)*cos(a)))**0.5
print(u)
print(G)