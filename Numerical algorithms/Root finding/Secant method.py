import matplotlib.pyplot as plt
import numpy as np
from math import *
points = []
p = 0

# Ввод:
print('Введите начало и конец отрезка, через пробел:',end = ' ')
a, b = map(float, input().split(' '))
n = int(input('Введите кол-во итераций: '))
eps_x = float(input('Введите eps по х: '))
eps_y = float(input('Введите eps по y: '))
h = float(input('Введите шаг: '))


# Табличка:
def W():
    print('''
Справка:
0 - ошибок допущено не было
1 - превышение количества итераций
n - число итераций''')
    print('\n№ Корня |  A  |  B  |  Корень  |   f(x)   |\
  n  | Код ошибки')

 
# Функция:    
def f(x):
    #f = np.sin(x)*x#x*x - x - 2
    f = np.sin(x)
    return f

# Вычисление способом секущих:
W() 
b1 = a
a1 = a
m, it = 0, 0
if h == 3:
    h -= 1
    p = 1
    
def s(u):
    if f(2) == sin(2) and u != 0:
        u *= 1.5
    return u
for i in range(int((b - a)//h)):   
    b1 += h
    a1 = b1 - h
    if b1 != 0:
        if f(a1) * f(b1) <= 0:
            xstart = a1
            xend   = b1
            while abs(abs(xstart)-abs(xend)) >= eps_x or abs(abs(f(xstart))-abs(f(xend))) >= eps_y:
                xp = xstart - f(xstart)*(xend - xstart)/(f(xend)-f(xstart))
                xstart, xend = xp, xstart
                it += 1
            points.append(xp)
            m += 1
            if p == 1:
                print('{:^8}|{:^5.1f}|{:^5.1f}|'. format(m,s(a1),s(b1)),sep = '|',end='')
            else:
                print('{:^8}|{:^5.1f}|{:^5.1f}|'. format(m,a1,b1),sep = '|',end='')
            if it > n:
                code = '1'
                print('{:^10}|{:^10}|{:^5}|\
{:^10}'. format('---','---',it,code),sep = '|')
            else:
                code = '0'
                print('{:^10.5f}|{:^10.6f}|\
{:^5}|{:^10}'. format(xp,f(xp),it,code),sep = '|')

# График:       
points = np.array(points)        
x1 = np.linspace(a,b,1000)
x = np.arange(f(a), f(b+h), h)
plt.figure(1)
plt.plot(x1,f(x1),color='y', linewidth=2.0)
plt.plot(points ,f(points),'go')
plt.grid(True)
plt.title('$Kulish$')
plt.ylabel('$y=f(x)$')
plt.subplot(111).spines['bottom'].set_position('zero')
print('\n',' '*20,'Enter=Пуск!',end='')
i = input()
plt.show()














