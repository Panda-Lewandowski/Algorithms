def f(x):
    return x**x


def simpson38 (a,b,n):
    h = abs(b-a)/n
    S = 0
    while a-b<-h/2:
        S += f(a)+3*f(a+h/3)+3*f(a+2*h/3)+f(a+h)
        a += h
    return S*h/8