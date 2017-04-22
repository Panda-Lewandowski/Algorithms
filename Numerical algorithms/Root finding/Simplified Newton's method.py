import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)
def p(x):
    return np.cos(x)

a = -10
b = 10
h = 1
points = []
eps = 0.001

n = 0
b1 = a
a1 = a
for i in range(int((b - a)//h)):
    b1 += h
    a1 = b1 - h
    if b1 != 0:
        if f(a1) * f(b1) <= 0:
            xstart = a1
            xend = b1
            while abs(abs(xstart)-abs(xend)) >= eps:
                xp = xstart - f(xstart)/p(a1)
                xstart,xend = xp,xstart
            n += 1
            points.append(xp)
            print(n,'=',xp)
    

plt.figure('Добрый день')
points = np.array(points)
x1 = np.linspace(a,b,1000)
plt.plot(x1,f(x1),color='g', linewidth=1.0)
plt.plot(points,f(points),'ro')
plt.subplot(111).spines['bottom'].set_position('zero')
plt.title('$Kuznetsov$')
plt.ylabel('$y=sin(x)$')
plt.grid(True)
plt.show()

