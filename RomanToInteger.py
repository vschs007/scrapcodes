def valuetoint(roman):
    value={
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
    }
    p = 0
    ans = 0
    n = len(roman)
    for i in range(n - 1, -1, -1):
        if (value[roman[i]]>=p):
            ans+=value[roman[i]]
        else:
            ans-=value[roman[i]]

        p= value[roman[i]]

    print(ans)


valuetoint('MCMIV')