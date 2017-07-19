import random
import time

N = 10000

def std_shell_sort(x):
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
        gap = gap_prev * 3 + 1

    while gap >= 1:
        i = gap
        while i <= len(x) - 1:
            if x[i] < x[i - gap]:
                x[i], x[i - gap] = x[i - gap], x[i]
                sorte = True
            i = i + 1
        if sorte == False:
            gap = (gap - 1) // 3
        sorte = False
    return x


def opt_shell_sort(x):
    inc = len(x) // 2
    while inc:
        for i, el in enumerate(x):
            while i >= inc and x[i - inc] > el:
                x[i] = x[i - inc]
                i -= inc
            x[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
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
    na = std_shell_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_shell_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_shell_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_shell_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_shell_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_shell_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_shell_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")
