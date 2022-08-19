def fd(arr,i,sm):
    if i >=len(arr):
        return sm
    else:
        return max(arr[i]+fd(arr,i+2,sm),fd(arr,i+1,sm))
t = int(input())
cnt = 1
while (t):
    n = int(input())
    arr = list(map(int, input().split()))

    print(f"Case {cnt}: {fd(arr,0,0)}")
    t -= 1
    cnt+=1
