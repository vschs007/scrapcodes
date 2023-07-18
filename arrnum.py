t = int(input())
while (t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(len(arr)-1,1,-1):
        if arr[i]%arr[i-1]==0 and arr[i]!=arr[i-1]:



    t -= 1