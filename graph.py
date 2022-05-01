#imports
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    #math function
    return ((-1/15)*x**5)+((3/2)*x**4)-((37/3)*x**3)+(46*x**2)-((771/10)*x)+59

xPoints=np.arange(0,8,0.01)
yPoints=[]
for i in xPoints:
    yPoints.append(round(f(i),3))

yw=np.empty(len(xPoints))
yw.fill(18)

fig, ax =plt.subplots(figsize=(12,6),sharex=True)
plt.plot(xPoints,yPoints,color='blue',label='graph data')
plt.plot(xPoints,yw,color='red',label='Yw')

plt.grid()
plt.show()