import random
import time

N = 1000


def std_bubble_sort(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[j], x[i] = x[i], x[j]
    return x


def opt_bubble_sort(x):
    n = len(x)
    while n != 0:
        newn = 0
        for i in range(1, n):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                newn = i

            n = newn
    return x


if __name__ == "__main__":
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(i)
        b.append(N-i)
        c.append(random.randint(-N, N))

    print("NO OPTIMIZED std_bubble_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = std_bubble_sort(a)
    end = time.time()
    print(na, "\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_bubble_sort(b)
    end = time.time()
    print(nb, "\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_bubble_sort(c)
    end = time.time()
    print(nc, "\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_bubble_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_bubble_sort(a)
    end = time.time()
    print(na, "\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_bubble_sort(b)
    end = time.time()
    print(nb, "\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_bubble_sort(c)
    end = time.time()
    print(nc, "\nTIME:", (end - st), "  sec")
