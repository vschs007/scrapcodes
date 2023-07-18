def selectopt(arr, i, sm):
    if i >= len(arr):
        return 0
    else:
        return max(selectopt(arr, i + 1, sm), arr[i] + (selectopt(arr, i + 2, sm)))


t = int(input())
cnt = 1
while (t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = []
    for i in range(len(arr)):
        res.append(selectopt(arr, i, 0))
    print(f"Case {cnt}: {max(res)}")
    t -= 1
    cnt += 1
