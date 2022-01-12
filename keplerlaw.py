t = int(input())
while(t):
    arr=list(map(int,input().split()))
    if pow(arr[0],2)/pow(arr[2],3) == pow(arr[1],2)/pow(arr[3],3):
        print("Yes")
    else:
        print("No")
    t-=1