t= int(input())
while(t):
    n,k =map(int,input().split())
    opp = list(map(int,input().split()))
    my = list(map(int,input().split()))

    if max(opp)>max(my):
        print("NO")
    elif max(opp)< max(my):
        print("YES")
        print(*sorted(my))

    if max(my)==max(opp):
        maxopp = max(opp)
        if opp.index(maxopp) == len(opp)-1:
            newmy = sorted(my)
            if len(newmy)>1:
                temp = newmy[-1]
                newmy[-1]= newmy[-2]
                newmy[-2]=temp
                print("YES")
                print(*newmy)
            if len(newmy)==1:
                print("NO")
        else:
            refopp = opp
            newarr=[0]*len(my)
            

    t-=1

