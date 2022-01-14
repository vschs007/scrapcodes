s = "a"
t = "a"
n = len(s)
ws=1
while(ws<=n):
    for i in range(n):
        if i+ws<=n+1:
            tempstr = s[i:i+ws]
            one = "".join(sorted(tempstr))
            two ="".join(sorted(t))
            if two in one:
                print(tempstr)
                exit()
            continue
        else:
            i+=1
    ws+=1
#above is brute force approach

