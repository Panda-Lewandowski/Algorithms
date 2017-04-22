import random
def sort (x):
    if len(x) <= 1:
        return(x)
    else:   
        q = x[len(x) // 2]
        l = []
        m = []
        r = []
        for i in range(len(x)):
            if x[i] < q:
                l.append(x[i])
            elif x[i] == q:
                m.append(x[i])
            else:
                r.append(x[i])

        return(sort(l) + m + sort(r))


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
