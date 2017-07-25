# Beware of Carmichael numbers
import random
import time

random.seed()

k = 0
level_of_security = 128 # 2^-128


def std_is_prime(x):
    global k

    lvl = k
    if x == 2:
        return True
    while lvl < level_of_security:

        rnd = random.randint(1, x - 1)

        if (rnd ** (x - 1) % x != 1):
            return False

        lvl += 1

    return True


def opt_is_prime(x):
    global k

    lvl = k
    if x == 2:
        return True
    while lvl < level_of_security:
        rnd = random.randint(1, x - 1)
        if gcd(rnd, x) != 1:
            return False
        if pows(rnd, x - 1, x) != 1:
            return False

        lvl += 1

    return True


def gcd(a, b):  # Euclidean algorithm
    if not b:
        return a

    return gcd(b, a % b)


def mul(a, b, mod):  # Binary mul with mod
    if b == 1:
        return a
    if not b % 2:
        t = mul(a, b / 2, mod)
        return (2 * t) % mod

    return (mul(a, b - 1, mod) + a) % mod


def pows(a, b, mod):  # Binary pow with mod
    if b == 0:
        return 1
    if not b % 2:
        t = pows(a, b / 2, mod)
        return mul(t, t, mod) % mod

    return (mul(pows(a, b-1, mod), a, mod)) % mod


if __name__ == "__main__":
    test_set = [2, 11, 7, 561, 23, 199, 3539, 8, 150, 4045, 2663]
    p = 17471

    print("...NOT OPTIMAZED...")

    for t in test_set:
        print("Is {0}  prime? ->".format(t), std_is_prime(t))

    st = time.time()
    res = std_is_prime(p)
    end = time.time()
    if res:
        print("Found the prime number was detected for ", end - st, " sec")
    else:
        print("Test crached!")

    print("\n\n...OPTIMAZED...")

    for t in test_set:
        print("Is {0}  prime? ->".format(t), opt_is_prime(t))

    st = time.time()
    res = opt_is_prime(p)
    end = time.time()
    if res:
        print("Found the prime number was detected for ", end - st, " sec")
    else:
        print("Test crached!")