import random
def sort (x):
    for i in range(1, len(x)):
        key = x[i]
        left = 0
        right = i
        while right > left:
            mid = int(left+right) // 2
            if x[mid] < key:
                left = mid+1
            else:
                right = mid-1

        for j in range(i-1, left-1, -1):
            x[j+1] = x[j]
        x[left] = key

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
