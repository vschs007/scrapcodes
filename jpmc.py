def bf(n):
    a = []
    while n != 1 and n not in a:
        a.append(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

print(bf(19))
