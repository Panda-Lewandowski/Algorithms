import random
import time

N = 100000


def std_comb_sort(x):
    gap = len(x)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(x) - gap):
            j = i+gap
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
                swaps = True

    return x


def opt_comb_sort(x):
    l = len(x)
    gap = (l * 10 // 13) if l > 1 else 0
    while gap:
        if 8 < gap < 11:  ## variant "comb-11"
            gap = 11
        swapped = False
        for i in range(l - gap):
            if x[i + gap] < x[i]:
                x[i], x[i + gap] = x[i + gap], x[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped

    return x



if __name__ == "__main__":
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(i)
        b.append(N-i)
        c.append(random.randint(-N, N))

    print("NO OPTIMIZED std_comb_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = std_comb_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_comb_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_comb_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_comb_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_comb_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_comb_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_comb_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")
