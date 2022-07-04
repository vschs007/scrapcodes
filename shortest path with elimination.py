def kaamkafunction(s,k):
    if  k>len(s) or len(s)==0:
        return 0
    mp={}
    for item in s:
        if item in mp:
            mp[item]+=1
        else:
            mp[item]=1

    resstr = 0
    start = 0
    isinvalid = False

    for i in range(len(s)):
        if mp[s[i]] <k:
            resstr = max(resstr,kaamkafunction(s[start:i],k))
            start=i+1
            isinvalid =True
    if not isinvalid:
        return len(s)
    else:
        return max(resstr,kaamkafunction(s[start:],k))








print(kaamkafunction("aaabb",3))