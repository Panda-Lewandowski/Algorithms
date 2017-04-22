def f(x):
    return x**x


def trap(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += (f(a)+f(a+h))/2
        a += h
    return S*h