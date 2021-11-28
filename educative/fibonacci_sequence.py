def fib(n):
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    step = 3

    while step <= n:
        fib_n = first + second
        first = second
        second = fib_n

        step += 1
    return fib_n


print(fib(5))
