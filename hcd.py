import  collections
t = int(input())
cnt=1
while(t):
    flag= False
    n,k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int,input().split()))
    lst =dict(collections.Counter(arr))
    if n/k >2:
        flag=True
    for k in lst.values():
        if k>2:
            flag = True
            break
    if flag:
        print(f'Case #{cnt}: NO')
    else:
        print(f'Case #{cnt}: YES')



    # mp1={}
    # mp2={}
    # for k in arr:
    #     if k not in mp1 and len(mp1)<=k:
    #         mp1.





    cnt+=1
    t-=1