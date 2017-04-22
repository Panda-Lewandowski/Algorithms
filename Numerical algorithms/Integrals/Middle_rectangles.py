def f(x):
    return x**x

def centr(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += f((2*a+h)/2)
        a += h
    return S*h