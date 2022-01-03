t = int(input())
while(t):
    temp = list(map(int,input().split()))
    n=temp[0]
    k =temp[1]
    if n-(2*k)+1<0:
        print(-1)
        t-=1
        continue
    arr=[]
    for i in range(n):
        col = []
        for j in range(n):
            col.append(".")
        arr.append(col)
    i=0
    c=0
    j=0
    while(i<n and j<n and c<k):
        arr[i][j]='R'
        i+=2
        j+=2
        c+=1
    if i<=n+2 and j<=n+2:
        for i in range(n):
            print(*arr[i],sep="")
    else:
        print(-1)
    t-=1

