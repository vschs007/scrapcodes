def findxor(n):
    mod = n%4
    if mod ==0:
        return n
    elif mod==1:
        return 1
    elif mod==2:
        return n+1
    elif mod==3:
        return 0
t= int(input())
while(t):
    n,x = map(int,input().split())
    if x==5*pow(10,5):
        xxx=findxor(n-2)
        for i in range(1,n-1):
            print(str(i),end=" ")
        ans1 = pow(2,17)
        for i in range(17):
            k = xxx>>i
            if (k&1):
                ans1+=pow(2,i)
        print(str(ans1)+" "+str(500000-pow(2,17)))
        continue
    if x > 100000:
        if n%4==0:
            for i in range(1,n):
                print(str(i),end=" ")
            print(x)
        elif n%4==1:
            for i in range(0,n-1):
                print(str(i),end=" ")
            print(x)
        elif n%4==2:
            for i in range(1,n):
                print(str(i),end=" ")
            if x%2==0:
                print(x+1)
            else:
                print(x-1)
        else:
            for i in range(0,n-1):
                print(str(i),end=" ")
            if x%2==0:
                print(x+1)
            else:
                print(x-1)
    else:
        if n%4==0:
            if x==1:
                for i in range(3,n):
                    print(str(i),end=" ")
                print("262143 131072 131069")
                continue
            xx= pow(10,5) +3+1
            for i in range(0,n-2):
                xx+=1
                print(str(xx),end=" ")
            print("0 ")
            if x%2==0:
                print(x+1)
            else:
                print(x-1)
        elif n%4==1:
            xx =pow(10,5)+3+1
            for i in range(0,n-1):
                xx+=1
                print(str(xx)+" ",end=" ")
            print(x)
        elif n%4==2:
            xx = pow(10, 5) + 3 + 1
            for i in range(0,n-2):
                xx+=1
                print(str(xx),end=" ")
            print(str(x)+" 0")
        else:
            xx= pow(10,5)+3+1
            for i in range(0,n-1):
                print(str(xx),end=" ")
            if x%2==0:
                print(x+1)
            else:
                print(x-1)
    t-=1
