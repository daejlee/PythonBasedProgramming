def factorial_iter(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret


def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)

print(factorial_iter(5), factorial_recur(5))