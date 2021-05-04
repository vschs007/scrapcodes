# cook your dish here
t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int, input()))
    l = len(arr)
    counta = 0
    c = 0
    countb = 0
    ca = 0
    cb = 0
    for i in range(2 * n):
        if (i % 2 == 0):
            ca += 1
            if (arr[i] == 1):
                counta += 1
        if (i % 2 != 0):
            cb += 1
            if (arr[i] == 1):
                countb += 1

        if (counta - countb > n - cb):
            print(i + 1)
            c = 1
            break
        if (countb - counta > n - ca):
            print(i + 1)
            c = 1
            break
    if (c == 0):
        print(2 * n)
