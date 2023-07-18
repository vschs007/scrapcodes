t = int(input())
while (t):
    n = int(input())
    s = input()
    dct = {}
    res = ""
    if n % 2 != 0:
        print("NO")
    else:
        for i in s:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1

        mx = max(dct.values())
        if mx <= n // 2:
            print("YES")
            tmp = sorted(dct, key=dct.get, reverse=True)
            # print(dct)
            for k in tmp:
                 #  print(k)
                res += k * dct.get(k)
            print(res)
        else:
            print("NO")
            # print(mx)
    t -= 1
