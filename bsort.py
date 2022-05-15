arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            arr[i] , arr[j] = arr[j],arr[i]

print(arr)