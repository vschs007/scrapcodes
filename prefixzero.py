t = int(input())
while(t):
    n,k = map(int,input().split())
    s=input()
    res=0
    count=0
    lst=[]
    strlist =list(s)
    for i in range(n):
        lst.append(10-int(strlist[i]))

    for i in range(n):
        if lst[i]!=10:
            res+=lst[i]
        else:
            res+=0
        if res<=k:
            count+=1
        else:
            break
    print(count)
    t-=1