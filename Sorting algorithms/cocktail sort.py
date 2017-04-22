import random

def sort (x):
    left = 0
    right = len(x)-1

    while left <= right:
        for i in range(left, right):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        right = right - 1

        for i in range(right, left, -1):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
        left = left + 1

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
