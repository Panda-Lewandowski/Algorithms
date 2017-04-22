import random
def sort (x):
    gap_prev = 1
    gap = 1
    sorte = True
    while True:
        if gap == len(x):
            break
        elif gap > len(x):
            gap = gap_prev
            break
        gap_prev = gap
        gap = gap_prev*3+1

    while gap >= 1:
        i = gap
        while i <= len(x)-1:
            if x[i] < x[i-gap]:
                x[i], x[i-gap] = x[i-gap], x[i]
                sorte = True
            i = i+1
        if sorte == False:
            gap = (gap - 1) // 3
        sorte = False
    return(x)


a = []
b = []
c = []
for i in range(100):
    a.append(i)
    b.append(100-i)
    c.append(random.randint(-100, 100))

a = sort(a)
b = sort(b)
c = sort(c)

print(a)
print(b)
print(c)
