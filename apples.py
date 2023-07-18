n = int(input())
arr = list(map(int, input().split()))
maxsofar = 0
res = 0
i = 0
while (i < n):
    res = arr[i]
    for j in range(0, n):
        if arr[j] < arr[i]:
            if j < i:
                continue
            else:
                res=0
                break
        else:
            if i != j and j>i or i-j==1:
                res += arr[i]
    maxsofar = max(res, maxsofar)

    i += 1
print(maxsofar)
