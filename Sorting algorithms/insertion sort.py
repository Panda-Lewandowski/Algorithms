import random
def sort (x):
    for i in range(1, len(x)):
        key = x[i]
        j = i-1
        while (j >= 0) and (x[j] > key):
            x[j+1] = x[j]
            j = j-1
        x[j+1] = key

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
