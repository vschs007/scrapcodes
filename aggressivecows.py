def possible(arrr, n,k):
    count=1
    for i in range(1, len(arrr)):
        start = 0
        if abs(arrr[i] - arrr[start]) >= n:
            start = i
            count += 1
            i=start+1
        else:
            continue
    if count == k:
        return True
    else:
        return False

n,k = map(int,input().split())
arr = list(map(int, input().split(",")))
sz = len(arr)
arr.sort()
low = 0
ans=-1
high = arr[sz - 1] - arr[0]
while(low<=high):
    mid = low + (high-low)//2
    if (possible(arr, mid,k)):
        ans = mid
        low = mid + 1

    else:
        high = mid - 1

print(ans)



