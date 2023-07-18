def countset(n):
    count =0
    while(n):
        n &= (n-1)
        count+=1
    return count


def setBitCount (L, K):
    #trivial solution
    res = countset(L)
    #need to subtract this.
    if res >=K:
        return L
    else:
        K = K-res
    R = L+1
    while(True):
        temp = countset(R)
        if temp >= K:
            return R
        else:
            K-=temp
            R+=1
print(setBitCount(9,5))