import random
import time

N = 1000


def std_counting_sort(x):
    i = 1
    while i < len(x):
        if not i or x[i - 1] <= x[i]:
            i += 1
        else:
            x[i], x[i - 1] = x[i - 1], x[i]
            i -= 1
    return x


def opt_counting_sort(x):
    i, j, size = 1, 2, len(x)
    while i < size:
        if x[i - 1] <= x[i]:
            i, j = j, j + 1
        else:
            x[i - 1], x[i] = x[i], x[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1

    return x


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
    nc = std_counting_sort(c)
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
    nc = opt_counting_sort(c)
    end = time.time()
    print(nc == sorted(c))
    print("\nTIME:", (end - st), "  sec")
