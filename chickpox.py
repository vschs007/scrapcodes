t = int(input())
while(t):
    n,k = map(int,input().split())
    res= (2*k)-1
    if k==0:
        print(n)
    elif k==n:
        print(res)
    else:
        print(res+(n-k)+1)



    t-=1