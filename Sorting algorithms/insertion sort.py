import random
import time

N = 1000


def std_insection_sort (x):
    for i in range(1, len(x)):
        key = x[i]
        j = i-1
        while (j >= 0) and (x[j] > key):
            x[j+1] = x[j]
            j = j-1
        x[j+1] = key

    return x


def opt_insection_sort(x):
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

    return x


if __name__ == "__main__":
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(i)
        b.append(N-i)
        c.append(random.randint(-N, N))

    print("NO OPTIMIZED std_insection_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = std_insection_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = std_insection_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = std_insection_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n\nOPTIMIZED opt_insection_sort(x)")

    print("\n...SORTING ARRAY...")
    st = time.time()
    na = opt_insection_sort(a)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...REVERSE ARRAY...")
    st = time.time()
    nb = opt_insection_sort(b)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")

    print("\n...RANDOM ARRAY...")
    st = time.time()
    nc = opt_insection_sort(c)
    end = time.time()
    print("\nTIME:", (end - st), "  sec")
