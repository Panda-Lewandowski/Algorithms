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
                c = (xend + xstart)/2
                if f(xstart)*f(c) <= 0:
                    xend = c
                else:
                    xstart = c
            n += 1
            points.append(c)
            print(n,'=',c)
    

plt.figure('Добрый день')
points = np.array(points)
x1 = np.linspace(a,b,1000)
plt.plot(x1,f(x1),color='g', linewidth=1.0)
plt.plot(points,f(points),'ro')
plt.subplot(111).spines['bottom'].set_position('zero')
plt.title('$Kulish$')
plt.ylabel('$y=sin(x)$')
plt.grid(True)
plt.show()

