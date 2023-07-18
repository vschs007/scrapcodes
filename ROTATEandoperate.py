def minDiffSubArray(arr, n):
    total_sum = 0
    for i in range(n):
        total_sum += arr[i]
    prefix_sum = 0
    minDiff = 999999

    # Traverse the given array
    for i in range(n - 1):
        prefix_sum += arr[i]
        diff = abs((total_sum -prefix_sum) -prefix_sum)
        if (diff < minDiff):
            minDiff = diff
    return minDiff

arr = [1,2,3,4]
t1 =[[1,1],[1,3],[2,2]]   #1 means right rotate, 2 means left rotat
finares=[]
for i in range(len(t1)):
    if t1[i][0] ==1:
        tempresarr = arr[-t1[i][1]:]+arr[:-t1[i][1]]
        print(tempresarr)
        finares.append(minDiffSubArray(tempresarr,len(tempresarr)))
    elif t1[i][0] ==2:
        tempresarr =  arr[t1[i][1]:] + arr[:t1[i][1]]
        finares.append(minDiffSubArray(tempresarr,len(tempresarr)))

print(finares)