import random
import time
from collections import defaultdict

N = 1000


def std_counting_sort(x, mn=0, mx=N):
    n = len(x)
    m = mx + 1
    count = [0] * m
    for a in x:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            x[i] = a
            i += 1
    return x


def opt_counting_sort(x, mn=0, mx=N):
    count = defaultdict(int)
    for i in x:
        count[i] += 1
    result = []
    for j in range(mn, mx + 1):
        result += [j] * count[j]
    return result


if __name__ == "__main__":
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(i)
        b.append(N - i)
        c.append(random.randint(-N, N))

    print("NO OPTIMIZED std_shell_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = std_counting_sort(a)
    end = time.time()
    print(na == sorted(a))
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_counting_sort(b)
    end = time.time()
    print(nb == sorted(b))
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_counting_sort(c, mn=-N, mx=N)
    end = time.time()
    print(nc == sorted(c))
    print("\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_shell_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_counting_sort(a)
    end = time.time()
    print(na == sorted(a))
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_counting_sort(b)
    end = time.time()
    print(nb == sorted(b))
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_counting_sort(c, mn=-N, mx=N)
    end = time.time()
    print(nc == sorted(c))
    print("\nTIME:", (end - st), "  sec")
