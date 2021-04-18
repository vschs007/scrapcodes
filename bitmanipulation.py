l,ts = map(int,input().split())
arr=list(map(int,input().split()))
flag=0
for i in range(l-1,0,-1):
    if(arr[i]==ts):
        print(i+1)
        flag=1
        break
if(flag==0):
    print(-1)

