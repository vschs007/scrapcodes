t=int(input())
for i in range(t):
    n,k = map(int,input().split(" "))
    arr=list(map(int,input().split(" ")))
    for x in reversed(arr):
        k-=k%x
    print("Case #"+str(i+1)+": "+str(k))
