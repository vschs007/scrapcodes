t= int(input())
while(t):
    n=int(input())
    b=[]
    arr= list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            b.append(arr[i]&arr[j])
    while(len(b)>1):
        maxb= max(b)
        minb=min(b)
        b.remove(maxb)
        b.remove(minb)
        b.append(maxb|minb)
    print(b[0])
    t-=1
