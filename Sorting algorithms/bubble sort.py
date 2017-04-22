import random

def sort (x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[j], x[i] = x[i], x[j]
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
