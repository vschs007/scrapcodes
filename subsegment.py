t= int(input())
while(t):
    n=int(input())
    even = 2
    odd=3
    for i in range(n):
        print(even,end=" ")
        if (i & 1):
            even+=3
        else:
            even+=1
    print()
    t-=1