t = int(input())
while (t):
    n = int(input())
    ip = list(map(int, input().split()))
    flg= True
    newip = sorted(ip)
    for i in range(1,n):
        if  newip[0]!=1 and newip[i]%newip[0]!=0:
            flg = False
            break
        if newip[0]==1:
    if flg ==True:
        print(n)
    else:
        print(0)


    t -= 1
