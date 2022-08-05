t = int(input())
while(t):
    n = int(input())
    res = [0] * n
    low =0
    high = n-1
    while(low<=high):
        res[low]=n
        if n ==1:
            break
        low+=1
        n-=1
        res[high]=n
        if n==1:
            break
        high-=1
        n-=1
    print(*res)
    t-=1
