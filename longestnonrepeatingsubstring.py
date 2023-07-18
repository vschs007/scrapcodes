s ="aab"
currlen  = maxlen =0
ans = ""
for c in s:
    if c in ans:
        index = ans.index(c)
        ans = ans[index + 1:]
        currlen = len(ans)
    ans = ans + c
    currlen+=1
    maxlen = max(currlen, maxlen)
print(maxlen)
