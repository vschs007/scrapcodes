t = int(input())
while(t):
    newarr=[]
    n,k = map(int,input().split())
    starting=list(map(int,input().split()))
    finalram = list(map(int,input().split()))

    for i in range(n):
        newarr.append([starting[i],finalram[i]])
    newarr = sorted(newarr, key = lambda x: x[0])
    for i in range(n):
        if k >= newarr[i][0] and newarr[i]!=-1:
            k+=newarr[i][1]
            newarr[i]=-1
            i=0
        else:
            continue
    print(k)
    t-=1