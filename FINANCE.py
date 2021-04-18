def Is(arr, n):
    for i in range(n):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1

        arr[j] = temp
    return arr


N = int(input())
A = list(map(int, input().split()))
unsor=[x for x in A]
sorarr = Is(A, N)
for a in unsor:
    print(sorarr.index(a) + 1,end=" ")