def simpson(func, *args, right, left, n):
    h = (right - left) / n

    ans = h / 3
    even = 0.0
    odd = 0.0

    for i in range(1, n):
        if i % 2 == 0:
            even += func(left + h * i, *args)
        else:
            odd += func(left + h * i, *args)

    ans *= (2 * even + 4 * odd + func(left, *args) + func(right, *args))
    return ans
