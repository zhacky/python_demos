def pell(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    c = 0
    for i in range(3, n + 1):
        c = (b * 2) + a
        a = b
        b = c

    return b





    return result