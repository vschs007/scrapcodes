t =int(input())
while(t>0):
    count=0
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if a[0] >=b[0]:
        count+=1
    for i in range(1,len(a)):
        if a[i]-a[i-1] >= b[i]:
            count+=1
        else:
            continue
    print(count)
    t-=1
