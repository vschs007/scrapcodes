t= int(input())
while(t):
    m,x = map(int,input().split())
    if m==2:
        resarr=[]
        for i in range(1,x+1):
            resarr.append(1)
        print(*resarr)
    elif m%2!=0:
        if x<m:
            resarr=[]
            for i in range(1,x+1):
                resarr.append(1)
            print(*resarr)
        else:
            resarr=[]
            for i in range(1,m):
                resarr.append(i)
            for i in range(m,x+1):
                resarr.append(m-1)
            print(*resarr)
    elif m%2==0  and m!=2:
        resarr=[]
        if x<=m-2:
            for i in range(1,x+1):
                resarr.append(i)
            print(*resarr)
        else:
            resarr=[]
            for i in range(1,m-2+1):
                resarr.append(1)
            for i in range(m-1,x+1):
                resarr.append(2)
            print(*resarr)
    t-=1










