a=[2,3,4]
c=[3,4,3]
la=len(a)
arr=[]
for i in range(la):
    possible=True
    aval=a[i]
    for j in range(la):
        curr=(i+j)%la
        next=(curr+1)%la
        aval=aval-c[curr]
        if(aval<0):
            possible =False
            break
        else:
            aval = aval + a[next]
    if(possible):
        arr.append(i)
    else:
        arr.append(-1)

arr=(list(set(arr)))
arr.remove(-1)
if(len(arr) !=0):
    print(min(arr))
else:
    print(-1)






