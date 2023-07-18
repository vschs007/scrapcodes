t = int(input())
while(t):
 #   dino=[]
    n, k = map(int, input().split())
    if n==2:
        print(1,2)
        t-=1
        continue
    else:
    #    rem = 0
        lst=[x for x in range(1,n+1)]
        ref =lst
        for i in range(1,k):
            if i==1:
                lst[1]=lst[2]
            if (i+2)%n==1:
                lst[i]=lst[2]
            elif (i+2)%n==n:
                lst[i]=lst[2]
            else:
                lst[i] = lst[(i+2)%n]
            #lst = lst[::2] + lst[1::2]
            print(lst)
            #print(lst[0])
    print(*lst)
    t-= 1
