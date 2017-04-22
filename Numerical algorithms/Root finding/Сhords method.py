from math import sin
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def horda(x1, x2, E, Nconst):
    t1 = x2
    t2 = x1
    N = 0
    while abs(t1 - t2) > E and N <= Nconst:
        if N != 0:
            t1 = t2
        N += 1
        t2 = t1 - (f(t1)/(f(t1) - f(x1)))*(t1 - x1)
    return t1, N , 0

def hordb(x1, x2, E, Nconst):
    t1 = x1
    t2 = x2
    N = 0
    while abs(t1 - t2) > E and N <= Nconst:
        if N != 0:
            t1 = t2
        N += 1
        t2 = t1 - f(t1)*(x2 - t1)/(f(x2) - f(t1))
    return t1, N , 0

a = float(input('Введите первую границу: '))
b = float(input('Введите вторую границу; '))
h = float(input('введите шаг: '))
E = float(input('Введите точность: '))
Nconst = int(input('Введите максимальное число итераций: '))
  
T = []

# n - номер корня
n = 0
x = a - h
d = b - a

if ((d)/h)%1 != 0:
    r = int((d)/h) + 1
else:
    r = int((d)/h)
    
for i in range(r):
    x += h
    if i == r - 1:
        h = int(d) - h*(r - 1)
    N = 0  # N - число итераций
    if abs(f(x)) < E:
        if x == a:
           n += 1
        k = x
        t = [n, x, x + h, k, N, 1]
        T.append(t)
    elif abs(f(x + h)) < E:
        n += 1
        k = x + h
        t = [n, x, x + h, k, N, 1]
        T.append(t)
    else:
    
        if f(x)/abs(f(x)) != f(x + h)/abs(f(x + h)):
            qk = (f(x) - f(x + h))/(-h)
            qb = (x*f(x + h) - (x + h)*f(x))/(-h)
            x0 = (-qb)/qk
            
            if f(x) > f(x + h):
                if f(x0) <= 0:
                    k, N, ko = horda(x, x + h, E, Nconst)
                        
                elif f(x0) > 0:
                    k, N, ko = hordb(x, x + h, E, Nconst)
                        
            elif f(x) < f(x + h):
                if f(x0) <= 0:
                    k, N, ko = hordb(x, x + h, E, Nconst)
                        
                elif f(x0) > 0:
                    k, N, ko = horda(x, x + h, E, Nconst)
                    
            n += 1
            t = [n, x, x + h, k, N, ko]
            T.append(t)        

# Вывод результатов
print()
if T == []:
    print('Корней нет.')
    
else:    
    print('N - номер корня     A         B          Корень         ', end = '')
    print('Число итераций     Код ошибки')
    
    for i in range(len(T)):
        n = T[i][0]
        A = T[i][1]
        B = T[i][2]
        k = T[i][3]
        N = T[i][4]
        ko = T[i][5]
        
        print('{:6d}{:17.3f}{:10.3f}'.format(n, A, B), end = '')
        
        if k == int(k):
            k = int(k)
            
            print('{:11d}'.format(k), end = ' '*6)
            print('{:13d}{:17d}'.format(N, ko))
            
        elif 0 < abs(int(k)) < 10:
            print('{:15.6f}'.format(k), end = ' '*6)
            print('{:9d}{:17d}'.format(N, ko))
            
        else:
            print('{:17.6e}'.format(k), end = '')
            print('{:13d}{:17d}'.format(N, ko))
 
    print()
    print()    
    print('"Код ошибки" \n')
        
    print('0 - программа в полной мере выполняет свою', end = ' ')
    print('функцию (метод хорд применяется). \n')

    print('1 - значение корня совпало с одним из крайних значений')
    print('отрезка [A, B] (метод хорд не применяется).')

    k = [0, 0]
    x = np.linspace(a, b, 100)
    plt.plot(x, f(x), 'g')
    if T != []: 
        for i in range(len(T)):
            plt.plot(T[i][3], 0, 'yo', markersize = 8)
    plt.title('$Kuznetsov$')
    plt.ylabel('$f(x)$')
    plt.subplot(111).spines['bottom'].set_position('zero')
    plt.grid(True)
    plt.show()
