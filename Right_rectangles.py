def f(x):
    return x**x

def right(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        a += h
        S += f(a)
    return S*h
