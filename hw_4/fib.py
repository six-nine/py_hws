def fibonacci(n):
    if 1 <= n <= 2:
        return 1

    a = 1
    b = 1
    for _ in range(2, n):
        c = a + b
        a = b
        b = c

    return b


if __name__ == "__main__":
    # just to test
    print(fibonacci(int(input())))
