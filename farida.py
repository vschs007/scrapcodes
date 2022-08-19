def fd(arr):
    arr.append(0)
    arr.append(0)
    for i in range(len(arr)-3,-1,-1):
        if arr[i]+arr[i+2]>arr[i+1]:
            arr[i]+=arr[i+2]
        else:
            arr[i]=arr[i+1]
    return arr[0]

t = int(input())
cnt = 1
while (t):
    n = int(input())
    arr = list(map(int, input().split()))

    print(f"Case {cnt}: {fd(arr)}")
    t -= 1
    cnt+=1
