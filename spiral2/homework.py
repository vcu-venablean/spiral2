def spiralize(size, n=1):
    if size == 1:
        return n
    return 4 * n * n - 6 * n + 6 + spiralize(n - 2, n)


print(spiralize(1, 35))