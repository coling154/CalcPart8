

#Dependencies
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#define vars and function
#f(x)=(-1/15)*x^5+(3/2)*x^4-(37/3)*x^3+46*x^2-(771/10)*x+59
Yw=18

def f(x):
    return ((-1/15)*x**5)+((3/2)*x**4)-((37/3)*x**3)+(46*x**2)-((771/10)*x)+59

#find all values where Yw==f(x)
xPoints=np.arange(0,8,0.001)
yPoints=[]
for x in xPoints:
    yPoints.append(round(f(x),3))
#values of ints from desmos
# (0.943,18),(6.464,18)
point1=[0.943,18]
point2=[6.464,18]
yw=np.empty(len(xPoints))
yw.fill(Yw)


fx=lambda x:((-1/15)*x**5)+((3/2)*x**4)-((37/3)*x**3)+(46*x**2)-((771/10)*x)+59
I=integrate.quad(fx,point1[0],point2[0])
print((I[0])-Yw)