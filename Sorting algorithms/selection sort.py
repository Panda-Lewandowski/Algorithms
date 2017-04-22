import random
def sort (x):
    for i in range(len(x)):
        min_ind = i
        for j in range(i, len(x)):
            if x[min_ind] > x[j]:
                min_ind = j
        x[i], x[min_ind] = x[min_ind], x[i]

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
