def findmex(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] <= 1:
            continue
        elif arr[i] - arr[i - 1] not in [0, 1]:
            return arr[i - 1] + 1
    if (arr[0] > 0):
        return arr[0] - 1
    else:
        return (arr[-1] + 1)

arr = [1, 0, 3, 0, 1]
sarr = arr.copy()
sarr.sort()
res = -1
# generate subarray from the given subarray
for i in range(1, len(arr) - 1):
    k = findmex(arr[:i])
    l = findmex(arr[i:])
    if k == l:
        res = i
        break

if res > 0:
    print(res)
else:
    print(-1)
