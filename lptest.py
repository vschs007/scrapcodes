s= "bbbbd"
for i in range(1,len(s)):
    l=i-1
    r=i+1
    maxlen=0
    while(l>=0 and r<len(s) and s[l]==s[r]):
        lsr = r-l+1
        if maxlen < lsr:
            maxlen = lsr
            res = s[l:r+1]
            print(res)
        l-=1
        r+=1
