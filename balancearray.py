t= int(input())
while(t):
    n = int(input())
    a = list(map(int,input().split()))
    b=list(map(int,input().split()))
    sm = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            a[i],b[i] = b[i],a[i]
    for i in range(len(a)-1):
        sm+=(abs(a[i]-a[i+1]) + abs(b[i]-b[i+1]))
    print(sm)
    t-=1






