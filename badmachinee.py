t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    count = 0
    mn=2000000000
    for i in range(l):
        mn=min(mn,arr[i])
        count=count+mn
    print(count)


