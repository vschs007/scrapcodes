t= int(input())
while(t):
    n,a =map(int,input().split())
    if n==1:
        if a%2==0:
            print("Even")
        else:
            print("Odd")
    elif n>1:
        if a%2!=0:
            if n%2!=0:
                print("Odd")
            else:
                print("Even")
        elif a%2==0:
            print("Impossible")


    t-=1