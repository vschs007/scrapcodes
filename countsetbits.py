def countSetBits(n):
    count = 0
    while (n):
        n &= (n - 1)
        count = count + 1

    return count

l =9
res = countSetBits(l)
k=8
r=l+1
if res >= k:
    print(l)
while(True):
    if countSetBits(r) >= k - countSetBits(r-1):
        print(r)
        break
    else:
        k -= countSetBits(r)
        r+=1


