import math

t =int(input())
while(t):
    res=0
    curr=0
    n,i,j =map(int,input().split())
    if(i==j or i+j==n+1):
        res=0
    else:
        if i%2==0 or j%2==0:
            res=1


    print(res)

    t-=1