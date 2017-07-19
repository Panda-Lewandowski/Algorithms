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


def opt_insection_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]
    return seq


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
