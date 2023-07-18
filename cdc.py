t = int(input())
while(t):
    n,k = (map(int,input().split()))
    s=input()
    ans=0
    retans=0
    i=0
    j=0
    while(j<n):
        if (j-i+1)<k:
            ans^=int(s[j])
            j+=(n-k+1)
            continue
        if j-i+1==k:
            ans^=int(s[j])
            if ans==1:
                retans+=1
            i+=1
            j+=(n-k+1)
    print(retans)
    t-=1