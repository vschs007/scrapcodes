t = int(input())
while(t):
    n,k =map(int,input().split())
    s =input()
    # k=1
    # s="001100"
    n = len(s)
    i=0
    j=n-1
    cnt=0
    while(i<j):
        if s[i]!=s[j]:
            cnt+=1
            i+=1
            j-=1
        else:
            i+=1
            j-=1
            continue
    if cnt<=k:
        if n%2==0 and (k-cnt)%2==0:
            print("YES")
        if n%2!=0 and (k-cnt)%2!=0:
            print("YES")
    else:
        print("NO")
    t-=1