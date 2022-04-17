

#Dependencies
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#define vars and function
#f(x)=(-1/15)*x^5+(3/2)*x^4-(37/3)*x^3+46*x^2-(771/10)*x+59
Yw=18

def f(x):
    return (-1/15)*x**5+(3/2)*x**4-(37/3)*x**3+46*x**2-(771/10)*x+59

#find all values where Yw==f(x)
xPoints=np.arange(0,8,0.001)
yPoints=[]
for x in xPoints:
    yPoints.append(round(f(x),3))
#values of ints from desmos
# (0.943,18),(6.464,18)
point1=[0.943,18]
point2=[6.464,18]



#plot graph
fig, ax=plt.subplots(figsize=(12,6))
ax.plot(xPoints,yPoints,color='blue',label='graph data')
plt.axhline(y=Yw,color='red',label='Yw')
plt.plot(point1[0],point1[1],marker='o',markersize=5,markeredgecolor='black',markerfacecolor='green')
plt.plot(point2[0],point2[1],marker='o',markersize=5,markeredgecolor='black',markerfacecolor='green')

plt.grid()
plt.show()

