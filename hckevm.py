t=int(input())
while(t):
    res=list(map(int,input().split()))
    gainvotes=[]
    totvotes=[]
    a=res[0]
    b = res[1]
    c = res[2]
    p = res[3]
    q = res[4]
    r = res[5]
    # gainvotes.append(a)
    # gainvotes.append(b)
    # gainvotes.append(c)
    # gainvotes =sorted(gainvotes)
    # totvotes.append(p)
    # totvotes.append(q)
    # totvotes.append(r)
    tot=((p+q+r)//2)
    # mex = min(totvotes)

    if (p+b+c>tot or a+q+c>tot or a+b+r>tot):
    #if a+b+mex >tot or a+c+mex>tot or b+c+mex>tot:
        print("YES")
    else:
        print("NO")






    t-=1