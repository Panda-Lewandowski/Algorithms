from math import sin, cos
def f(x):
    return cos(x)

def fd(x):
    return -sin(x)

def fdd(x):
    return -cos(x)

# норм
def half(a, b, eps):
    c = (a + b) / 2
    if f(c) == 0:
        return c
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    while (b - a) >= eps:
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return c

# норм
def newton(a, b, eps):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    while abs(b - a) >= eps:
        a = b - f(b)/ fd(b)
        b = a - f(a)/fd(a)
    return (b + a)/2


# норм
def newton_imp(a, b, eps):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * fdd(a) > 0:
        fix = fd(a)
    else:
        fix = fd(b)
    while abs(b - a) >= eps:
        a = b - f(b)/ fix
        b = a - f(a)/ fix
    return a

# норм
def chord(a, b, eps):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * fdd(a) > 0:
        fix = a
        x = b
        h = ((x - fix) * f(x)) /(f(x) - f(fix))
    else:
        fix = b
        x = a
        h = ((x - fix) * f(x)) /(f(x) - f(fix))
    while abs(h) >= eps:
        x -= h
        h = ((x - fix) * f(x)) /(f(x) - f(fix))
    return x
        
        


# норм
def tan(a, b, eps):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    while abs(b - a) >= eps:
        a = b - f(b) * (a - b)/(f(a) - f(b))
        b = a - f(a) * (b - a)/(f(b) - f(a))
    return b

def comb(a, b, eps):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    while abs(a - b) >= eps:
        if f(a) * fdd(a) < 0:
            a -= (f(a) * (a - b))/(f(a) - f(b))
        else:
            a -= f(a)/fd(a)
        if f(b) * fdd(b) < 0:
            b -= (f(b) * (b - a))/(f(b) - f(a))
        else:
            b -= f(b)/fd(b)
    return (a + b)/2

def steffenson(a, b, eps):
    try:
        while abs(b - a) > eps and n >= 0:
            c = a - f(a)**2/(f(a + f(a)) - f(a))
            b = c
            a = (a+c)/2
        return c
    except:
        return '-'


def iteration(a, b, eps):   
    for x0 in [a,b]:
        
        #подбираем lambd
        #lmbd == false => lambda = 1
        #lmbd == true  => lambda = 1/fp(x)
        lmbd = False
        x1 = x0 - f(x0)
        x2 = x1 - f(x1)

        if abs(x2 - x1) > abs(x1 - x0):
            lmbd = True 
            if (fd(x1) == 0) or (fd(x0) == 0)  :
                return x1 
            x1 = x0 - f(x0)/fd(x0)
            x2 = x1 - f(x1)/fd(x1)
            if abs(x2 - x1) > abs(x1 - x0):
                return x1
            
        while True:   
            
            if not lmbd:
                x1 = x0 - f(x0)
            else:
                x1 = x0 - f(x0)/fd(x0)
            #условия завершения
            if eps > 0:
                if abs(x1 - x0) < eps:
                    return x1


def plotting1(key):
    global list_of_roots
    m = np.linspace(a, b, 1000)
    y = []
    z = []
    u = []
    for k in range(len(m)):
        y.append(f(m[k], key))
        z.append(f(m[k], 4))
        u.append(f(m[k], 5))
    for k in range(len(list_of_roots)):
        if k == 0:
            plt.scatter(list_of_roots[k], f(list_of_roots[k], key), marker='o', color='r', label='Roots')
        else:
            plt.scatter(list_of_roots[k], f(list_of_roots[k], key), marker='o', color='r')
    for k in range(len(ext)):
        if k == 0:
            plt.scatter(ext[k], f(ext[k], 0), marker='s', color='m', label='Extrema')
        else:
            plt.scatter(ext[k], f(ext[k], 0), marker='s', color='m')
    for k in range(len(bend)):
        if k == 0:
            plt.scatter(bend[k], f(bend[k], 0), marker='p', color='orange', label='Inflection')
        else:
            plt.scatter(bend[k], f(bend[k], 0), marker='p', color='orange')
    plt.plot(m, y, color='k', linewidth=1.0, label='x*sin(x) ')
    plt.plot(m, z, color='g', alpha=0.5, linewidth=1.0, label='The first derivative')
    plt.plot(m, u, color='pink', alpha=0.5, linewidth=1.0, label='The second derivative')
    plt.grid(True, color='b', linewidth=0.5)
    plt.axis([a, b, -15., 15.])
    plt.ylabel('f(x)', size=14)
    plt.xlabel('x', size=14)
    plt.legend(frameon=False)
    plt.title('The function, its the first and the second \nderivatives with points of inflection and extrema')
    plt.show()



v = 5
w = 7
ep = 0.0001
print('половинного  ', half(v, w, ep))
print('касательные ', newton(v, w, ep))
print('имп касательные ', newton_imp(v, w, ep))
print('хорды ',chord(v, w, ep))
print('сек ', tan(v, w, ep))
print('комб ', comb(v, w, ep))
print('стеффенсон ', steffenson(6, 7, ep))

    


        
    
    
    
    
