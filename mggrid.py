t=int(input())
while(t):
    n=int(input())
    for i in range(n):
        arr=[]
        for j in  range(n):
            arr.append(1)
        print(*arr)
    t-=1
