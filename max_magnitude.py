def solve(k, n):
    kdec = int(k, 16)
    ndec = int(n, 16)
    resdec = ndec % kdec
    return (hex(resdec))


t = int(input())
while (t > 0 and t < 11):
    k = input()
    n = input()
    print(solve(k, n))
    t = t - 1
