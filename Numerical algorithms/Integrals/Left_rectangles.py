def f(x):
    return x**x

def left(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += f(a)
        a += h
    return S*h